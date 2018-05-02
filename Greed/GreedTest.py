from Greed import Greed
from NoDiceException import NoDiceException
from NumberOfOccurrencesRule import NumberOfOccurrencesRule
from ThreePairsRule import ThreePairsRule
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
            NumberOfOccurrencesRule(die=1, number_of_occurrences=5, score=4000),
            NumberOfOccurrencesRule(die=2, number_of_occurrences=5, score=800),
            NumberOfOccurrencesRule(die=3, number_of_occurrences=5, score=1200),
            NumberOfOccurrencesRule(die=4, number_of_occurrences=5, score=1600),
            NumberOfOccurrencesRule(die=5, number_of_occurrences=5, score=2000),
            NumberOfOccurrencesRule(die=6, number_of_occurrences=5, score=2400),
            NumberOfOccurrencesRule(die=1, number_of_occurrences=6, score=8000),
            NumberOfOccurrencesRule(die=2, number_of_occurrences=6, score=1600),
            NumberOfOccurrencesRule(die=3, number_of_occurrences=6, score=2400),
            NumberOfOccurrencesRule(die=4, number_of_occurrences=6, score=3200),
            NumberOfOccurrencesRule(die=5, number_of_occurrences=6, score=4000),
            NumberOfOccurrencesRule(die=6, number_of_occurrences=6, score=4800),
            ThreePairsRule()
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
            # One-die combinations
            ([1], 100),
            ([2], 0),
            ([3], 0),
            ([4], 0),
            ([5], 50),
            ([6], 0),
            ([6], 0),

            # Two-dice combinations
            ([1, 5], 150),
            ([5, 1], 150),
            ([1, 1], 0),
            ([5, 5], 0),

            # Three-dice combinations
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
            ([1, 5, 6], 150),

            # Four-dice combinations
            ([1, 1, 1, 1], 2000),
            ([2, 2, 2, 2], 400),
            ([3, 3, 3, 3], 600),
            ([4, 4, 4, 4], 800),
            ([5, 5, 5, 5], 1000),
            ([6, 6, 6, 6], 1200),
            ([1, 2, 2, 2], 300),
            ([1, 3, 3, 3], 400),
            ([1, 4, 4, 4], 500),
            ([1, 5, 5, 5], 600),
            ([1, 6, 6, 6], 700),
            ([5, 1, 1, 1], 1050),
            ([5, 2, 2, 2], 250),
            ([5, 3, 3, 3], 350),
            ([5, 4, 4, 4], 450),
            ([5, 6, 6, 6], 650),

            # Five-dice combinations
            ([1, 1, 1, 1, 1], 4000),
            ([2, 2, 2, 2, 2], 800),
            ([3, 3, 3, 3, 3], 1200),
            ([4, 4, 4, 4, 4], 1600),
            ([5, 5, 5, 5, 5], 2000),
            ([6, 6, 6, 6, 6], 2400),
            ([2, 2, 2, 4, 4], 200),
            ([2, 2, 2, 1, 4], 300),
            ([2, 2, 2, 4, 5], 250),
            ([2, 2, 2, 1, 5], 350),
            ([2, 3, 2, 1, 5], 150),
            ([2, 2, 2, 2, 1], 500),
            ([2, 2, 2, 2, 5], 450),

            # Six-dice combinations
            ([1, 1, 1, 1, 1, 1], 8000),
            ([2, 2, 2, 2, 2, 2], 1600),
            ([3, 3, 3, 3, 3, 3], 2400),
            ([4, 4, 4, 4, 4, 4], 3200),
            ([5, 5, 5, 5, 5, 5], 4000),
            ([6, 6, 6, 6, 6, 6], 4800),
            ([1, 1, 2, 2, 3, 3], 800),
        )
    )
    def testItReturnsTheCorrectScoreDependingOnTheDice(self, dice, expected_score):
        score = self.greed.score(dice=dice)
        self.assertEqual(expected_score, score)
