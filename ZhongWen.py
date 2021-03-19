#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# s1 = 72
# s2 = 85
# r = (s2-s1)/s1*100
# name = '小明'
# print(f'{name}的成绩提升了 {r:.1f}%')
# print('%s的成绩提升了 %.1f%%' % ('小明', r))
# print('{0}的成绩提升了 {1:.1f}%'.format('小明', r))

# collegues = ['Mark','Tara','Jack','Faheem','Cici']
# print(len(collegues))
# print(collegues[0])
# print(collegues[-2])
# collegues.append('Mario')
# collegues.insert(2, 'Jeffrey')
# collegues[0] = 'Yuyi'
# print(collegues)

# def add(x, y, f):
#     return f(x) + f(y)

# print(add(-5, 6, abs))

# def f(x):
#     return x * x
# r = map(f, [1,2,3,4,5,6,7,8,9])
# print(list(r))

# s = list(map(str, [1,2,3,4,5,6,7,8,9]))
# print(s)

from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# def zhuanhua(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# a = reduce(fn, map(zhuanhua, '13579'))
# print(a)
# digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def zhuanhuan(s):
#     def fn(x, y):
#         return x * 10 + y
#     def zhuan(s):
#         return digits[s]
#     return reduce(fn, map(zhuan, s))
# print(zhuanhuan('12345'))

# def normalize(name):
#     L = name[:1].upper() + name[1:].lower()
#     return L
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def prod(L):
#     def zhuanhua(s):
#         return digits[s]
#     def pingfang(x, y):
#         return x * y
#     if type(L[0]) is str:
#         I = map(zhuanhua, L)
#         return reduce(pingfang, I)
#     else:
#         return reduce(pingfang, L)

# print('3 * 5 * 7 * 9 =', prod(['3', '5', '7', '9']))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

def str2float(s):
    n = s.index('.')
    def zhuanhua(s):
        return digits[s]
    def bian(x, y):
        return x * 10 + y
    return reduce(bian, map(zhuanhua, (s[:n]+s[n+1:])))/(10**n)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')