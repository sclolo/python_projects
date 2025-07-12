import locale
import pytz
import calendar
from datetime import datetime
import time

# si une locale manque
# id = fr par exemple
# sudo apt-get install language-pack-id 
# sudo dpkg-reconfigure locales

print (locale.getlocale())
locale.setlocale(locale.LC_ALL,'fr_FR')

cal = calendar.month(2019,8)
print(cal)

# d = date.today().__format__('%d %B %Y')
# print(d)
# d = datetime.(1968,10,2)
# t = datetime.now()

# t1 = t-d

# print(f'Il y a {t1.days} jours entre le {d.__format__('%d %B %Y')} et le {t.__format__('%d %B %Y')}')


while True:
    tz1 = pytz.timezone('Africa/Douala')
    dz1 = datetime.now(tz1)
    tz2 = pytz.timezone('Europe/Paris')
    dz2 = datetime.now(tz2)
    print(f'Heure de Douala {dz1.strftime('%H:%M:%S')}, heure de Paris {dz2.strftime('%H:%M:%S')}',end= "\r", flush= True)
    time.sleep(1)
    


