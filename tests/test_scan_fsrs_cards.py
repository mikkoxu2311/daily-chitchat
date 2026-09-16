import importlib.util
import tempfile
import subprocess
import json
import sys
import unittest
from datetime import datetime
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "scan_fsrs_cards.py"
SPEC = importlib.util.spec_from_file_location("scan_fsrs_cards", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ScanFsrsCardsTest(unittest.TestCase):
    def test_scans_unscheduled_and_overdue_cards(self):
        with tempfile.TemporaryDirectory() as directory:
            note = Path(directory) / "2026-01-01 English Speaking.md"
            original = """# English Speaking

## Flashcards

### Card 1 · build on

在已有基础上继续推进
?
**Chunk:** build on
**Example:** Let's build on yesterday's idea.

### Card 2 · fall short

结果没有达到预期
?
**Chunk:** fall short
**Example:** The result fell short.
<!--SR:!fsrs,2026-01-01T08:00:00Z,3,0.9,2025-12-29T08:00:00Z-->
"""
            note.write_text(original, encoding="utf-8")

            result = json.loads(subprocess.check_output([
                sys.executable, str(SCRIPT), directory,
                '--now', '2026-01-02T09:00:00+00:00'], text=True))

            self.assertEqual(result["counts"], {"new_unscheduled": 1, "overdue": 1})
            self.assertEqual(result["cards"][0]["chunk"], "build on")
            self.assertEqual(result["cards"][1]["schedule"]["status"], "overdue")
            self.assertEqual(note.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
