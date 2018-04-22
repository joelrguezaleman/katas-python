from Greed import Greed
from NoDiceException import NoDiceException
from unittest_data_provider import data_provider
import unittest

class GreedTest(unittest.TestCase):

    def setUp(self):
        self.greed = Greed()

    def testItRaisesAnExceptionIfItAttemptsToScoreWithoutDice(self):
        self.assertRaises(
            NoDiceException,
            self.greed.score,
            dice=[]
        )

    @data_provider(
        lambda: (
            (1, 100),
            (2, 0),
            (3, 0),
            (4, 0),
            (6, 0),
        )
    )
    def testItReturnsTheCorrectScoreDependingOnTheDice(self, die, expected_score):
        score = self.greed.score(dice=[die])
        self.assertEqual(expected_score, score)
