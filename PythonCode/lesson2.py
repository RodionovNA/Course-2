"""
лямбда функции
map первый арг функция, второй аргумент список
"""


# a = [1, 2, 3]
# b = list(map(lambda x: x ** 2, a))
# print(b)

# n = int(input())
# t = []
# for i in range(n):
#     t.append(i)
# print(t)
#
# #аналог функции выше
# a2 = [i for i in range(n)]
# print(a2)

# n = int(input())
# a = [i for i in range(n)]
# b = list(filter(lambda x: x % 2 == 0, a))
# print(b)

# a = (1, 2, 3) #кортеж
# a[2] = 1
# print(a)

# def changelist(a=[]):
#     a.append(2)
#     print(a)
#
# changelist()
# changelist()
# changelist()

# a = (1, 2, 3)
# b = list(a)

def fun(a, b = None):
    if b == None:
        return a
    else:
        return a + b

print(fun(1))