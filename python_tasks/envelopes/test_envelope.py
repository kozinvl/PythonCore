import unittest
from python_tasks.envelopes.envelope_2 import Envelope


class TestEnvelope(unittest.TestCase):
    def test_validation_negative(self):
        self.assertFalse(Envelope.is_validated(-1, 1))

    def test_validation_positive(self):
        self.assertTrue(Envelope.is_validated(5.0, 5.0))


if __name__ == '__main__':
    TestEnvelope()
