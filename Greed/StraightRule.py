class StraightRule:

    def validate(self, number_of):
        return 1200 if number_of.count(1) == 6 else 0
