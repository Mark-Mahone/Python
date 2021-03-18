import time, functools
# def odd(x):
#     return x % 2 == 1
# print(list(filter(odd, [1,2,3,4,5,6,7,8,9])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# def makejishu():
#     n=1
#     while True:
#         n = n + 2
#         yield n
# def xuansushu(n):
#     return lambda x: x % n > 0
# def sushu():
#     yield 2
#     it = makejishu()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(xuansushu(n), it)
# for n in sushu():
#     if n < 1000:
#         print(n)
#     else:
#         break

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
    
# output = filter(is_palindrome, range(1, 100000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def paiming(x):
#     return x[0]

# def fenshu(x):
#     return -x[1]

# L2 = sorted(L, key=paiming)
# print(L2)
# L3 = sorted(L, key=fenshu)
# print(L3)

# def createCounter():
#     x = 0
#     def counter():
#         nonlocal x
#         x = x + 1
#         return x
#     return counter

# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def nth_power(exponent):
#     def exponent_of(base):
#         return base ** exponent
#     return exponent_of # 返回值是 exponent_of 函数
# square = nth_power(2) # 计算一个数的平方
# cube = nth_power(3) # 计算一个数的立方
# print(square(2))  # 计算 2 的平方
# print(cube(2)) # 计算 2 的立方

# def build(x, y):
#     return lambda z: x * x + y * y + z

# print(build(2,3)(5))

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
# print(L)
# print(list(filter((lambda x: x % 2 == 1), range(1, 20))))

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('2015-3-25')
# print(now())

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s()' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     n = 1
#     print('2015-3-25')

# now()
# print(now.__name__)

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log(123)
def now():
    print('2021-3-5')
now()
print(now.__name__)

