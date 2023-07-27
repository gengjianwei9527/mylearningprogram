# -*- coding: utf-8 -*-
alien_color = 'green'
if alien_color == 'green':
    print('You have gained 5 points')

users = ['Gavin', 'zod', 'Admin', 'palm', 'android']
if users:
    for user in users:
        if user == 'Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello %s , welcome login' % user)
else:
    print('we need to add some users')
# 5-10 检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
# 创建一个至少包含5 个用户名的列表，并将其命名为current_users。
# 再创建一个包含5 个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users 中。
# 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，
# 就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
#  确保比较时不区分大消息；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。

current_users = ['Gavin', 'zod', 'Admin', 'palm', 'android', 'John', 'Humer']
new_users = ['Gavin1', 'Zod', 'Admin', 'palm', 'android1', 'JOHN']
currentlower_users = []
for current_user in current_users:
    currentlower_users.append(current_user.lower())
print(currentlower_users)
for new_user in new_users:
    if new_user.lower() in currentlower_users:
            print('this %s already in the current_users' % new_user)
    else:
        print('the new user %s can be registered' % new_user)

# 5-11 序数：序数表示位置，如1st 和2nd。大多数序数都以th 结尾，只有1、2 和3 例外。
# 在一个列表中存储数字1~9。遍历这个列表。
# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容
# 应为1st、2nd、3rd、4th、5th、6th、7th、8th 和9th，但每个序数都独占一行。
numbers = list(range(1, 10))
print(numbers)
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')
    