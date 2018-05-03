class NumberOfOccurrencesRule:

    def __init__(self, die, number_of_occurrences, score):
        self.die = die
        self.number_of_occurrences = number_of_occurrences
        self.score = score

    def validate(self, number_of):
        return self.score if number_of[self.die] == self.number_of_occurrences else 0
