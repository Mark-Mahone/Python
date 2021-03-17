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

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')