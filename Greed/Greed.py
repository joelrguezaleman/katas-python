from NoDiceException import NoDiceException

class Greed:

    def __init__(self, rules):
        self.rules = rules

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        number_of_occurrences_of = self._get_number_of_occurrences_of_dice(dice)
        return self._calculate_score(number_of_occurrences_of)

    def _get_number_of_occurrences_of_dice(self, dice):
        number_of_occurrences_of = [0, 0, 0, 0, 0, 0, 0]
        for die in dice:
            number_of_occurrences_of[die] = number_of_occurrences_of[die] + 1
        return number_of_occurrences_of

    def _calculate_score(self, number_of_occurrences_of):
        score = 0
        for rule in self.rules:
            score = score + rule.validate(number_of_occurrences_of)
        return score
