from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        return 0
