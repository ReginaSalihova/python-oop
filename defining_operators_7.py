class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def __add__(self, other):
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)
        if len_self > len_other:
            new_coefficients = self.coefficients.copy()
            for i in range(len_other):
                new_coefficients[i] += other.coefficients[i]
        else:
            new_coefficients = other.coefficients.copy()
            for i in range(len_self):
                new_coefficients[i] += self.coefficients[i]
        return Polynomial(new_coefficients)


poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()
