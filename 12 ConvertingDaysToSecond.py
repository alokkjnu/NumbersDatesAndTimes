# Converting Days to Seconds, and other Basic Time Conversion

from datetime import timedelta

a = timedelta(days = 2,hours=6)
b = timedelta(hours=4.5)
c = a+b
print(c)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)