from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        number_of_occurrences_of_dice = self._get_number_of_occurrences_of_dice(dice)
        return self._calculate_score(number_of_occurrences_of_dice)

    def _get_number_of_occurrences_of_dice(self, dice):
        number_of = [0, 0, 0, 0, 0, 0, 0]
        for die in dice:
            number_of[die] = number_of[die] + 1
        return number_of

    def _calculate_score(self, number_of):
        if 3 in number_of:
            die_number = number_of.index(3)
            return 1000 if die_number == 1 else die_number * 100
        if (number_of[1] == 1):
            return 150 if number_of[5] == 1 else 100
        if (number_of[5] == 1):
            return 50
        return 0
