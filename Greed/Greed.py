from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        return 100 if dice[0] == 1 else 0
