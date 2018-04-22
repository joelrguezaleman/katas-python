from NoDiceException import NoDiceException

class Greed:

    def score(self, dice):
        if not dice:
            raise NoDiceException()
        score = 0
        another_die_has_number_1_too = False
        for die in dice:
            if die == 1:
                score = score + (-100 if another_die_has_number_1_too else 100)
                another_die_has_number_1_too = True
            if die == 5:
                score = score + 50
        return score
