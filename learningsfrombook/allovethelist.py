# -*- coding: utf-8 -*-
animals = ['cat', 'dog', 'chicken', 'rabbit']
for animal in animals:
    print(animal)
    print(animal.title() +' ' + 'is in the house!')

for value in range(21):
    print(value)

L = list(range(1, 20, 2))
print(L)

L2 = list(range(3, 31, 3))
print(L2)

cubes = [value**3 for value in range(1,11)]
print(cubes)