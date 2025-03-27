import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return None 
        return x / y

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        if math.cos(x) == 0:
            return None  
        return math.tan(x)

    def square_root(self, x):
        if x < 0:
            return None  
        return math.sqrt(x)

    def power(self, x, y):
        return x ** y