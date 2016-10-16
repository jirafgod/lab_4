#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 2, 1, 1, 2, 12, 12, 1, 211]
data2 = gen_random(1, 3, 10)
data3 = ['K', 'O', 'S', 'T', 'Y', 'A', '', 'g', 'o', 'd']
# Реализация задания 2

print(list(Unique(data1)))

print(list(Unique(list(data2))))

print(list(Unique(data3, ignore_case=True)))
