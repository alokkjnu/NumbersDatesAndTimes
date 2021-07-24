# Working with Binary, Octal and Hexadecimal Integers

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))


x = -1234
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))
print(format(2**32 + x,'b'))
print(format(2**32 + x,'x'))
print(format(2**32 + x,'o'))

print(int('4d2', 16))
print(int('10011010010', 2))