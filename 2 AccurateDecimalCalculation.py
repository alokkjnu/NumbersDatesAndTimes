#Performing Accurate Decimal Calculation
a = 4.1
b = 2.1
print(a+b)
print((a+b)==6.3)

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
c = a+b
print(c)

print(a+b == Decimal('6.3'))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

