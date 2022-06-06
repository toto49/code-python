import os
import datetime



liste = os.listdir('/media/atom/TOM 2')
print(liste)

update = open('update.txt', 'a')
update.write(f'\n{datetime.datetime.now()}\n')
update.write(f'{liste}\n')

update.close()