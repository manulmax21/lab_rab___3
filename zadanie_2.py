#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b, c = map(int, input('Введите a, b, c через пробел: ').split())
D = b*b - 4*a*c

x = []

if D < 0:
    print('Действительных корней нет')
else:
    t1 = (-b+D**(1/2))/(2*c)
    t2 = (-b-D**(1/2))/(2*c)

    if t1 >= 0: x.append(t1**(1/2))
    if t2 >= 0: x.append(t2**(1/2))

    print('Действительные корни:', *x, sep=' '+chr(177))