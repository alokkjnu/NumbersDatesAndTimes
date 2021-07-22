# Calculating with Fractions

from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print(a+b)
print(a*b)

#Getting Numerator/Denomirator

c = a*b
print(c.denominator)

# Converting to a float
print(float(c))

# Limiting the Denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)