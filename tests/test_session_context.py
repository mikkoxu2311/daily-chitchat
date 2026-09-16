import importlib.util
from pathlib import Path
import unittest

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


if __name__ == '__main__':
    unittest.main()
