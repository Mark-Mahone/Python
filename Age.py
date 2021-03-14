import math

# -*- coding: utf-8 -*-

# print('hello, world')

# # age = int(input('Please enter yor age:\n'))
# # if age >= 18:
# #     print("You're Adult")
# # else:
# #     print("You're Teenager")

# # L = [
# #     ['Apple', 'Google', 'Microsoft'],
# #     ['Java', 'Python', 'Ruby', 'PHP'],
# #     ['Adam', 'Bart', 'Lisa']
# # ]
# # print(L[0][0])
# # print(L[1][1])
# # print(L[2][2])

# birth = int(input('birth: '))
# if birth < 2000:
#     print('OO前')
# else:
#     print('00后')

# height = int(input('请输入您的身高(cm): '))
# weight = int(input('请输入您的体重(kg): '))
# bmi = weight / (height/100)1**2
# if bmi > 32:
#     print('严重肥胖')
# elif bmi >= 28:
#     print('肥胖')
# elif bmi >= 25:
#     print('过重')
# elif bmi >= 18.5:
#     print('正常')
# else:
#     print('过轻')

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0 
# n = 1
# while n < 100:
#     sum = sum + n
#     n = n +2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('Hello, %s !' % x)

# n = 1
# while n <= 100:
#     if n > 20:
#         break
#     print(n)
#     n = n + 1
# print('END')

# n = 0
# while n < 100:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Mark'] = 100
# print(d.pop("Bob"))
# print(d)

# n1 = 255
# n2 = 1000
# print('%s转换为十六进制表示的字符串是： %s' % (n1, hex(n1)))
# print('%s转换为十六进制表示的字符串是： %s' % (n2, hex(n2)))

# def transfer(s):
#     if not isinstance(s, (int, float)):
#         raise TypeError('Bad in put')
#     if s > 0:
#         return s
#     else:
#         return -s
# print(transfer(-7))
# print(transfer("abs"))

# def quard(a,b,c):
#     x1 = ((-b) + math.sqrt(b**2 - 4 * a * c)) / (2*a)
#     x2 = ((-b) - math.sqrt(b**2 - 4 * a * c)) / (2*a)
#     return x1, x2
# print('一元二次方程ax2+bx+c=0的两个解为: ', quard(2,3,1))
# print('一元二次方程ax2+bx+c=0的两个解为: ', quard(1,3,-4))

# if quard(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quard(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# def xdencifang(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print(xdencifang(3,3))
# print(xdencifang(3))

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end())
# print(add_end([1,2,3]))

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(*[1,2,3]))
# print(calc(1,2,3))

# def product(*numbers):
#     x = 1
#     if len(numbers) > 0:
#         for y in numbers:
#             x = x * y
#         return x
#     else:
#         raise TypeError

# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(1000))

# def move(n, a, b, c):   #n个盘子从a移到c，b为辅助
#     if n==1:
#         print(a,'-->',c)
#     else:
#         move(n-1,a,c,b) #n-1个盘子从a移到b，c为辅助
#         move(1,a,b,c)   #最后1个盘子从a移到c
#         move(n-1,b,a,c) #n-1个盘子从b移到c，a为辅助
# move(6,'A','B','C')

# L = '我是二傻子'
# print(L[::3])

# def trim(s):
#     if type(s) is str:
#         while s[:1] == ' ':
#             s=s[1:]
#         while s[-1:] == ' ':
#             s=s[:-1]
#     else:
#         raise TypeError('数据类型不对')
#     return s

# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# d = {'a': 1, 'b': 2, 'c': 3}
# for k, v in d.items():
#     print(k,v)

def findMinAndMax(L):
    if not isinstance(L, (list)):
        raise TypeError('请输入一个list')
    else:
        if len(L) == 0:
            return (None, None)
        else:
            Max = Min = L[0]
            for x in L:
                if x >= Max:
                    Max = x
            for x in L:
                if x <= Min:    
                    Min = x
    return(Min, Max)

print(findMinAndMax([7, 1]))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')