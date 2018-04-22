from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        score = 0
        for die in dice:
            if die == 1:
                score = score + 100
            if die == 5:
                score = score + 50
        return score
