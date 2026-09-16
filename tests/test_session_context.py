import importlib.util
from pathlib import Path
import unittest
import tempfile

spec = importlib.util.spec_from_file_location('context', Path(__file__).parents[1] / 'scripts/session_context.py')
ctx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctx)


def target(name, state, selection=''):
    return f'### {name}\n\n- **State:** {state}\n- **Meaning:** A useful meaning.\n- **Source:** [[lesson#Evidence]]\n- **Selection:** {selection}\n\n'


class ContextTests(unittest.TestCase):
    def data(self, body):
        return {'queue': '## Active Review Targets\n\n' + body + '## Deepen Targets\n\n',
                'notes': {'lesson': '# Evidence\n'}}

    def test_retired_and_paused_never_enter_routine_selection(self):
        d=self.data(target('learn', 'learning') + target('check', 'ready_to_check') +
                    target('done', 'retired') + target('pause', 'learning', 'paused'))
        result=ctx.review_candidates(d)
        self.assertEqual([(x['expression'],x['mode']) for x in result],
                         [('learn','learning'),('check','transfer_check')])

    def test_broken_evidence_is_not_a_candidate(self):
        d=self.data(target('check','ready_to_check').replace('#Evidence','#Missing'))
        self.assertEqual(ctx.review_candidates(d), [])

    def test_old_states_require_evidence_migration(self):
        d=self.data(target('old','independent_once'))
        self.assertEqual(ctx.review_candidates(d), [])

    def test_fsrs_update_does_not_change_speaking_fingerprint(self):
        self.assertEqual(ctx.fingerprint({'lesson':'# Evidence\n'}),
                         ctx.fingerprint({'lesson':'# Evidence\n<!--SR:!fsrs,changed-->\n'}))

    def check_note(self, extra='', card=''):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory).resolve()
            (project / 'Sessions').mkdir()
            note = project / 'Sessions/lesson.md'
            note.write_text('---\nai_authored: true\nai_author: Codex\ncreated: 2026-01-01\n'
                            'human_reviewed: false\ntype: english-speaking-session\ndate: 2026-01-01\n'
                            'session_id: example-practice\ntopic: Example\nreview_status: completed\n'
                            'tags: [english-speaking]\n' + extra + '---\n# Evidence\n' + card)
            queue = '\n'.join('## ' + section + '\n' for section in ctx.LIMITS)
            data = {'project': str(project), 'queue': queue, 'warnings': [],
                    'notes': {'lesson': note.read_text()}, 'source_fingerprint': '', 'session_count': 1}
            return ctx.check(data, note)

    def test_compact_note_without_schema_or_count_is_valid(self):
        self.assertTrue(self.check_note()['ok'])

    def test_legacy_count_is_still_verified(self):
        self.assertTrue(self.check_note('handoff_schema: english-speaking-session-handoff/v2\ncards_added: 0\n')['ok'])
        self.assertIn('cards_added does not match physical cards', self.check_note('cards_added: 1\n')['errors'])

    def test_compact_note_still_checks_card_structure(self):
        card = '\n## Flashcards\n\n### Card 1 · test expression\n\nA cue\n?\n**Chunk:** test expression\n**Example:** Example sentence.\n'
        self.assertTrue(self.check_note(card=card)['ok'])
        self.assertIn('Invalid multiline card structure', self.check_note(card=card.replace('\n?\n', '\n'))['errors'])


if __name__ == '__main__':
    unittest.main()
