#!/usr/bin/env python3
"""Read Obsidian speaking cards and report their FSRS due state.

The scanner is deliberately read-only. It never writes scheduling metadata.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


CARD_RE = re.compile(
    r"^### Card[ \t]+\d+[ \t]+·[ \t]+(?P<title>.+?)[ \t]*$\n(?P<body>.*?)(?=^### Card[ \t]+\d+[ \t]+·|^##[ \t]|\Z)",
    re.MULTILINE | re.DOTALL,
)
SCHEDULE_RE = re.compile(r"<!--SR:!fsrs,(?P<data>[^>]+)-->")
CHUNK_RE = re.compile(r"^\*\*Chunk:\*\*[ \t]*(?P<chunk>.+?)[ \t]*$", re.MULTILINE)
EXAMPLE_RE = re.compile(r"^\*\*Example:\*\*[ \t]*(?P<example>.+?)[ \t]*$", re.MULTILINE)


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def schedule_state(raw: str | None, now: datetime) -> dict:
    if raw is None:
        return {"status": "new_unscheduled", "due_at": None, "reviewed_at": None}

    fields = raw.split(",")
    due_at = parse_timestamp(fields[0])
    local_due = due_at.astimezone(now.tzinfo)
    if due_at <= now:
        status = "overdue"
    elif local_due.date() == now.date():
        status = "due_later_today"
    else:
        status = "scheduled_future"

    reviewed_at = fields[-1] if fields and "T" in fields[-1] else None
    return {
        "status": status,
        "due_at": due_at.isoformat().replace("+00:00", "Z"),
        "due_at_local": local_due.isoformat(),
        "reviewed_at": reviewed_at,
        "interval": fields[1] if len(fields) > 1 else None,
        "raw": f"!fsrs,{raw}",
    }


def parse_card(note: Path, title: str, body: str, now: datetime) -> dict:
    chunk_match = CHUNK_RE.search(body)
    example_match = EXAMPLE_RE.search(body)
    schedule_match = SCHEDULE_RE.search(body)
    question = body.split("\n?\n", 1)[0].strip()
    schedule = schedule_state(schedule_match.group("data") if schedule_match else None, now)
    return {
        "title": title.strip(),
        "chunk": chunk_match.group("chunk").strip() if chunk_match else title.strip(),
        "cue": question,
        "example": example_match.group("example").strip() if example_match else None,
        "source_note": note.stem,
        "source_path": str(note),
        "schedule": schedule,
    }


def scan_sessions(sessions_dir: Path, now: datetime) -> dict:
    cards = []
    for note in sorted(sessions_dir.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        flashcards = re.search(r"^## Flashcards\s*$\n(?P<body>.*)\Z", text, re.MULTILINE | re.DOTALL)
        if not flashcards:
            continue
        for match in CARD_RE.finditer(flashcards.group("body")):
            cards.append(parse_card(note, match.group("title"), match.group("body"), now))

    counts: dict[str, int] = {}
    for card in cards:
        status = card["schedule"]["status"]
        counts[status] = counts.get(status, 0) + 1

    return {
        "scanned_at": now.isoformat(),
        "sessions_dir": str(sessions_dir),
        "counts": counts,
        "cards": cards,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sessions_dir", type=Path)
    parser.add_argument("--now", help="ISO timestamp for deterministic testing")
    args = parser.parse_args()

    if not args.sessions_dir.is_dir():
        parser.error(f"sessions directory does not exist: {args.sessions_dir}")

    now = parse_timestamp(args.now).astimezone() if args.now else datetime.now().astimezone()
    print(json.dumps(scan_sessions(args.sessions_dir, now), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
