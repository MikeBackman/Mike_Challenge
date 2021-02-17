import math

class Complex(object):
    
    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)        
    
    #Complex addition of (a + bi) + (c + di) = (a+c) + (b+d)i
    def __add__(self, no):
        return Complex(self.real+no.real, self.imag+no.imag)
    #Complex subtraction of (a + bi) - (c + di) = (a-c) + (b-d)i
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imag-no.imag)
    #Complex multiplication of (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imag*no.imag, self.real*no.imag+self.imag*no.real)
    #Complex division of (a + bi) / (c + di) = (ac + bd) + (bc - ad)i * 1/c^2 + d^2 and in this case we can utilize our mod() function and square the result 
    def __truediv__(self, no):
        try:
            return self.__mul__(Complex(no.real, -1*no.imag)).__mul__(Complex(1.0/(no.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print (e)
            return None
    #Complex modulus(absolute value) of (a + bi) = sqrt(a^2 + b^2)
    def mod(self):
        return Complex(pow(self.real**2+self.imag**2, 0.5), 0)


    def __str__(self, precision=2):
        if self.imag == 0:
            result = "%0.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%0.2fi" % (self.imag)
            else:
                result = "0.00-%0.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%0.2f+%0.2fi" % (self.real, self.imag)
        else:
            result = "%0.2f-%0.2fi" % (self.real, abs(self.imag))

        return result

if __name__ == '__main__':
    c = Complex(*map(float, input().split()))
    d = Complex(*map(float, input().split()))
    print(*map(str, [c+d, c-d, c*d, c/d, c.mod(), d.mod()]), sep='\n')