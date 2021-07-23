# Converting Strings into Datetimes

from datetime import datetime
text = '2021-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
deff = z-y
print(deff)

print(z)
