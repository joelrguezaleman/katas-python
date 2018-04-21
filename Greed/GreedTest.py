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
            (2,),
            (3,),
            (4,),
            (6,),
        )
    )
    def testItReturnsZeroForAThrowWithASingleDieThatIsNotAOneOrAFive(self, die):
        score = self.greed.score(dice=[die])
        self.assertEqual(0, score)
