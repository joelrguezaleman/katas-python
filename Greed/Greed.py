from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        return self._handle_throw(dice)

    def _handle_throw(self, dice):
        number_of = [0, 0, 0, 0, 0, 0, 0]
        for die in dice:
            if die == 1:
                number_of[1] = number_of[1] + 1
            if die == 5:
                number_of[5] = number_of[5] + 1
        return self._calculate_score(number_of)

    def _calculate_score(self, number_of):
        if (number_of[1] == 3):
            return 1000
        if (number_of[1] == 1):
            return 150 if number_of[5] == 1 else 100
        if (number_of[5] == 1):
            return 50
        return 0
