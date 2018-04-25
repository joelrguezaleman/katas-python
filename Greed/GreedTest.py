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
            ([5, 1], 150),
            ([1, 1], 0),
            ([5, 5], 0),
            ([1, 3, 4], 100),
            ([1, 1, 4], 0),
            ([1, 1, 1], 1000),
            ([5, 3, 4], 50),
        )
    )
    def testItReturnsTheCorrectScoreDependingOnTheDice(self, dice, expected_score):
        score = self.greed.score(dice=dice)
        self.assertEqual(expected_score, score)
