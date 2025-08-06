"""Answer 1"""
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,address):
        self.name=name
        self.salary=salary
        self.address=address

p = Programmer("Dhrumil",70000000,"Junagadh")
# print(f"Our best employee is Mr.{p.name} his annual package is {p.salary} and he belong's to {p.address}")

"""Answer 2"""
import math

class Calculator:
    def square(self, a):
        return a ** 2  # or math.pow(a, 2)

    def cube(self, a):
        return a ** 3  # or math.pow(a, 3)

    def square_root(self, a):
        return math.sqrt(a)
    @staticmethod
    def greet():
        print("Hello :)")

c = Calculator()
print(f"{c.greet()},Square: {c.square(2)}, Cube: {c.cube(2)}, Square Root: {c.square_root(4)}")