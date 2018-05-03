class ASingleOccurrenceRule:

    def __init__(self, die, score, straight_rule):
        self.die = die
        self.score = score
        self.straight_rule = straight_rule

    def validate(self, number_of):
        score_for_straight_rule = self.straight_rule.validate(number_of)
        return self.score if number_of[self.die] == 1 and score_for_straight_rule == 0 else 0
