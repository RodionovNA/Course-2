"""
Выводятся песочный часы через циклы
"""


print("*" * 7)
for i in range(1, 4):
    if i == 3:
        print(" " * i + "*")
    else:
        print(" " * i + "*" + " " * (7 - 2 - i * 2) + "*")
for i in range(2, 0, -1):
    print(" " * i + "*" + " " * (7 - 2 - i * 2) + "*")
print("*" * 7)
