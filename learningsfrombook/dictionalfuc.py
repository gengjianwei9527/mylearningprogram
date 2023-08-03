# -*- coding: utf-8 -*-
classmates = {'First_name' : 'Qiang', 'Last_name' : 'Wang', 'Age' : 34, 'City' : 'NJ'}
print(classmates['First_name'] + '.' + classmates['Last_name'] + ' ' + str(classmates['Age']) + ' ' + classmates['City'])

lucky_numbers = {'Liming' : 5, 'Quattro' : 4, 'Gavin' : 8, 'Benz' : 300}
for k, v in lucky_numbers.items():
    print('\nName:', k)
    print('Luckynumber:', v)
for name in lucky_numbers.keys():
    print(name.title())