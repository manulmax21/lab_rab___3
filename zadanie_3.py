#!/usr/bin/env python3
# -*- coding: utf-8 -*-
i =input('Введите число: ')
print('Да' if int(i)%sum(map(int, list(i)))==0 else 'Нет')