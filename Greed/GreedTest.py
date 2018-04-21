from Greed import Greed
from NoDiceException import NoDiceException
import unittest

class GreedTest(unittest.TestCase):

    def testItRaisesAnExceptionIfItAttemptsToScoreWithoutDice(self):
        greed = Greed()
        self.assertRaises(
            NoDiceException,
            greed.score,
            dice=[]
        )
