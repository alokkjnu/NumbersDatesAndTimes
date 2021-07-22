#Formatting Numbers for Output

x = 1234.56789
#Two decimal places of occurancy
print(format(x,'0.2f'))

#Right Justified in chars, one digit occurancy
print(format(x,'>10.1f'))

#left Justified in chars, on digit occurancy
print(format(x,'<10.1f'))

#Center Justified in chars, on digit occurancy
print(format(x,'^10.1f'))

#Inclusion of thousand seprator
print(format(x,','))
print(format(x,'0,.1f'))

#Use of exponantial notation
print(format(x,'e'))
print(format(x,'0.2E'))
print('the value is {:0,.2f}'.format(x))