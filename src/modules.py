class TheOne():
    def __init__(self) -> None:
        pass

    def add_one(self, num):
        return num + 1

    def minus_one(self, num):
        return num - 1

    def multiple_one(self, num):
        return num * 1

    def divide_one(self, num):
        return num / 1

    def even_plus_one(self, num):
        if num % 2 == 0:
            return num + 1
        else:
            return None
