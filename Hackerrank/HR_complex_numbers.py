import math


class Complex(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return f"{self.real+no.real:.2f}+{self.imaginary+no.imaginary:.2f}i"

    def __sub__(self, no):
        r1 = self.real - no.real
        r2 = self.imaginary - no.imaginary
        return f"{r1:.2f}{r2:.2f}i"


    def __mul__(self, no):
        r1 = self.real * no.real - self.imaginary * no.imaginary
        r2 = self.real * no.imaginary + self.imaginary * no.real
        return f"{r1:.2f}+{r2:.2f}i"


    def __truediv__(self, no):
        r1 = self.real * no.real + self.real * no.imaginary + self.imaginary * no.imaginary
        r2 = self.real * no.imaginary + self.imaginary * no.real
        return f"{self.real}+{self.imaginary}i"


    def mod(self):
        pass
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')





exit(0)

# -1-5j
# expected:
#5.09901951359
#-1.76819188664
import cmath

a = input().split('+')

print(abs(complex(float(a[0]), float(a[1][:1]))))
print(cmath.phase(complex(float(a[0]), float(a[1][:1]))))



