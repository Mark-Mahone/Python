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

<<<<<<< HEAD
# L = []
# for x in range(1,11):
#     L.append(x*x)
# print(L)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() if isinstance(x, str) else x for x in L1]
# L3 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)
# print(L3)

# g = (x * x for x in range(1,11))
# for x in g:
#     print(x)

# def fib(x):
#     n, a, b = 0, 0, 1
#     while n < x:
#         yield(b)
#         t = (b, a+b)
#         a = t[0]
#         b = t[1]
#         n = n + 1
#     return 'done'
# for n in fib(888):
#     print(n)

def triangles():
    L = [1]
    while True:
        yield L[:]
        L.append(0)
        L = [L[n] + L[n-1] for n in range(len(L))]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
=======
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
<<<<<<< HEAD
    print('测试失败!')
=======
    print('测试失败!')

L = list(range(100))
print(L[:4])
print(L[4:])
>>>>>>> d4425948fa00ca4f59044f04b9c35b6352a50bbb
>>>>>>> cee8018ce441b42d50a8f021cf013ca9f42a7199
