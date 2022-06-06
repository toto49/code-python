import os
import datetime



liste = os.listdir('chemin du dossier que vous voulez lister')
print(liste)

update = open('update.txt', 'a')
update.write(f'\n{datetime.datetime.now()}\n')
update.write(f'{liste}\n')

update.close()
