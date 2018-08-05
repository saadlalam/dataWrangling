'''
Mingling with data 01
Story that never happened : Christmas is almost here, and wanted to buy a Christmas tree
but since I live far from Paris, and I work from 09h to 19h it is impossible to do so.
'''
import csv

sapins = list(csv.DictReader(open(r"PATH_TO\csv\points-de-collectes-des-sapins.csv")))

#set comprehension to check the dates :
sample = {row["HORAIRES"] for row in sapins}
print(f'{len(sample)} different working hours found  : ')
print(sample)

#Shops that open at 08 a.m
print('*'*50)
open_early = [row['ADRESSE'] for row in sapins if row["HORAIRES"].startswith('de 8h')]
print(f' {len(open_early)} shops open at 8 a.m : ')
print(open_early)
print('*' * 50)
#open 24h/24
all_day = [row['ADRESSE'] for row in sapins if row["HORAIRES"] == "ouvert 24h/24"]
print(f'{len(all_day)} are open 24h/24 :')
print(all_day)
print('*' * 50)
# in 16 area
in_area05 = [row['ADRESSE']
             for row in sapins if row["ARRONDISSEMENT"] == "75016"]
print(f'We found {len(in_area05)} shops located in Paris 75016 : ')
print(in_area05)
