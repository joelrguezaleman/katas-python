class ThreePairsRule:

    def validate(self, number_of):
        return 800 if number_of.count(2) == 3 else 0
