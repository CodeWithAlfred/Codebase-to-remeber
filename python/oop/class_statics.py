# THESE ARE FUNCTIONS INSIDE A CLASS THAT DO A SPECIFIC TASK< LIKE CONSTANT FUNCTiONS

class Math:
    @staticmethod
    def add1(x):
        return x + 1

    def add_5(x):
        return x + 5


print(Math.add_5(10))
