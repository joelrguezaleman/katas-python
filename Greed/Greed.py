from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        number_of_dice = len(dice)
        if number_of_dice == 0:
            raise NoDiceException()
        if number_of_dice == 1:
            return self._handle_a_throw_of_one_die(dice[0])
        if number_of_dice == 2:
            return self._handle_a_throw_of_two_dice(dice)
        return self._handle_a_throw_of_three_dice(dice)

    def _handle_a_throw_of_one_die(self, die):
        if die in [2, 3, 4, 6]:
            return 0
        return 100 if die == 1 else 50

    def _handle_a_throw_of_two_dice(self, dice):
        return 150 if (dice == [1, 5] or dice == [5, 1]) else 0

    def _handle_a_throw_of_three_dice(self, dice):
        number_of_ones = dice.count(1)
        if (number_of_ones == 1):
            return 100
        if (number_of_ones == 3):
            return 1000
        return 0
