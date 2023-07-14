# -*- coding: utf-8 -*-
# 3-8 放眼世界：想出至少5 个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
mostwantedplaces = ['tibet', 'xinjiang', 'sichuan', 'taishan', 'yulongxueshan']
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python 列表。
print(mostwantedplaces)
# 使用sorted()按字母顺序打印这个列表，同时不要修改它。
print('sorted list %s' % sorted(mostwantedplaces))
# 再次打印该列表，核实排列顺序未变。
print('The list now %s' % mostwantedplaces)
# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print('sorted list reverse %s' % sorted(mostwantedplaces, reverse=True))
# 再次打印该列表，核实排列顺序未变。
print('The list now %s' % mostwantedplaces)
# 使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
mostwantedplaces.reverse()
print('reverse the list: %s' % mostwantedplaces)
# 使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
mostwantedplaces.reverse()
print('reverse, the list change back to origin: %s' % mostwantedplaces)
# 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
mostwantedplaces.sort()
print('sort the list: %s' % mostwantedplaces)
# 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
mostwantedplaces.sort(reverse=True)
print('sort reverse the list: %s' % mostwantedplaces)

guestlists = ['A', 'B','C', 'D']
for guestlist in guestlists:
    print('Guest %s is invite to the party' % guestlist)
print('Guest C is not available to attend the party and guest E is coming')
guestlists[2] = 'E'
for guestlist in guestlists:
    print('Guest %s is invite to the party' % guestlist)
print('There is bigger table can have more people to invite')
guestlists.insert(0, 'a')
guestlists.insert(2, 'b')
guestlists.append('c')
for guestlist in guestlists:
    print('Guest %s is invite to the party' % guestlist)
print('There are %s guests in the list' % len(guestlists))
RM1 = guestlists.pop(1)
print('Guest %s will be removed in the list' % RM1)
RM2 = guestlists.pop(2)
print('Guest %s will be removed in the list' % RM2)
RM3 = guestlists.pop(2)
print('Guest %s will be removed in the list' % RM3)
RM4 = guestlists.pop(2)
print('Guest %s will be removed in the list' % RM4)
RM5 = guestlists.pop(2)
print('Guest %s will be removed in the list' % RM5)
print(guestlists)
for guestlist in guestlists:
    print('Guest %s is remaning in the party' % guestlist)
guestlists.remove('a')
guestlists.remove('b')
print(guestlists)
