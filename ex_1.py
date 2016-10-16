#!/usr/bin/env python3
from librip.gen import *
from librip.iterators import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
# Реализация задания 1
print(list(field(goods, 'title', 'color')))
print(list(gen_random(1, 4, 5)))
