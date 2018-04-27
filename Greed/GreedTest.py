from Greed import Greed
from NoDiceException import NoDiceException
from NumberOfOccurrencesRule import NumberOfOccurrencesRule
from unittest_data_provider import data_provider
import unittest

class GreedTest(unittest.TestCase):

    def setUp(self):
        rules = [
            NumberOfOccurrencesRule(die=1, number_of_occurrences=1, score=100),
            NumberOfOccurrencesRule(die=5, number_of_occurrences=1, score=50),
            NumberOfOccurrencesRule(die=1, number_of_occurrences=3, score=1000),
            NumberOfOccurrencesRule(die=2, number_of_occurrences=3, score=200),
            NumberOfOccurrencesRule(die=3, number_of_occurrences=3, score=300),
            NumberOfOccurrencesRule(die=4, number_of_occurrences=3, score=400),
            NumberOfOccurrencesRule(die=5, number_of_occurrences=3, score=500),
            NumberOfOccurrencesRule(die=6, number_of_occurrences=3, score=600),
            NumberOfOccurrencesRule(die=1, number_of_occurrences=4, score=2000),
            NumberOfOccurrencesRule(die=2, number_of_occurrences=4, score=400),
            NumberOfOccurrencesRule(die=3, number_of_occurrences=4, score=600),
            NumberOfOccurrencesRule(die=4, number_of_occurrences=4, score=800),
            NumberOfOccurrencesRule(die=5, number_of_occurrences=4, score=1000),
            NumberOfOccurrencesRule(die=6, number_of_occurrences=4, score=1200),
        ]
        self.greed = Greed(rules)

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
            ([5, 5, 4], 0),
            ([5, 5, 5], 500),
            ([2, 2, 2], 200),
            ([3, 3, 3], 300),
            ([4, 4, 4], 400),
            ([6, 6, 6], 600),
            ([1, 1, 1, 1], 2000),
            ([2, 2, 2, 2], 400),
            ([3, 3, 3, 3], 600),
            ([4, 4, 4, 4], 800),
            ([5, 5, 5, 5], 1000),
            ([6, 6, 6, 6], 1200),
        )
    )
    def testItReturnsTheCorrectScoreDependingOnTheDice(self, dice, expected_score):
        score = self.greed.score(dice=dice)
        self.assertEqual(expected_score, score)
