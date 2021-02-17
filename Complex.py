#In an OOP style, we created a child Complex class which inherits methods from the parent class complex
class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self)
    
if __name__ == '__main__':
    
    C = Complex(complex(2,1))
    D = Complex(complex(5,6))

    print("C + D =", C.__add__(D))
    print("C - D =", C.__sub__(D))
    print("C * D =", C.__mul__(D))
    print("C / D =", C.__truediv__(D))
    print("mod(C) =", C.mod())
    print("mod(D) =", D.mod())