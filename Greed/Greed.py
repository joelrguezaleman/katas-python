from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        if (dice[0] == 1):
            return 100
        elif (dice[0] == 5):
            return 50
        else:
            return 0
