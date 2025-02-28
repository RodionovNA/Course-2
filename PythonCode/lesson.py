"""
название функции с малеленькой буквы через прочерк
возвращает кортеж функция
функции являются объектами
сначала пишутся нбязательные аргументы
*args, **kwargs - args собирает неименованные объекты(кортеж), а kwargs именованые(словарь)
pop() по умолчанию последний элемент или по индексу
"""

import copy


def my_add_and_odd(a, b, c=None):
    """
    my function makes a+b
    :param c: third count
    :param b: second param
    :param a: first count
    :return: result of a+b
    """
    return a + b + c, a - b - c


def fun(*args, **kwargs):
    """
    :param args:
    :param kwargs:
    """
    print(args, kwargs)


print(fun(1, 2, 3, c=4, d=5))


a = [1, 2, 3]
b = [3, 4, a]
c = copy.deepcopy(b)

a.append(5)
b.append(12)

a.remove(1)
a.insert(0, 5)

if 1 in a:
    print(a.index(1))
a.sort(reverse=True)

h = b.pop()

a.extend(b)
print(a)


tmp = [1, 2]
a = [1, 2, 3, tmp]
b = a[:]    # аналог верхнеуровнего копорования
c = a[:]
tmp.append(1)
a.append(2)
print("b", b) # глубокое копирование позволяет рекурсивно копировать все mutable объекты, 
                #а поверхностное копирует только верхний слой, а указатели на mutable объекты остаются и если в этих muta   ble объектах что-то 
                    #меняется то эти изменения также отображаются в объектах которые были скопированы поверхностно
print("a", a)
print("c", c)
