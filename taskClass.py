class BasicCalculator:

    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number

obj = BasicCalculator(10,5)
print(obj.addition())
print(obj.subtraction())
print(obj.multiplication())
print(obj.division())