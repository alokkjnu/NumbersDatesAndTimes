# Manipulating Dates Involving Time Zones

from datetime import date, datetime, timedelta
from pytz import timezone
import pytz

d = datetime(2021,12,21,9,30,0)
print(d)

# Localize the date for India
central = timezone('ASIA/KOLKATA')
loc_d = central.localize(d)
print(loc_d)

later = loc_d + timedelta(minutes=30)
print(later)

later2 = central.normalize(loc_d + timedelta(minutes=30))
print(later2)

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

