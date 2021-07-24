# Working with Binary, Octal and Hexadecimal Integers

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))

x = -1234
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))
print(format(2**32 + x,'b'))
print(format(2**32 + x,'x'))
print(format(2**32 + x,'o'))

