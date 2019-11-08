class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(cls, year):
        return cls(2019-year)