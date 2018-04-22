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
            ([1], 100),
            ([2], 0),
            ([3], 0),
            ([4], 0),
            ([5], 50),
            ([6], 0),
            ([6], 0),
            ([1, 5], 150),
        )
    )
    def testItReturnsTheCorrectScoreDependingOnTheDice(self, dice, expected_score):
        score = self.greed.score(dice=dice)
        self.assertEqual(expected_score, score)
