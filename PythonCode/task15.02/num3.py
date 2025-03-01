"""
Выводится поле чисел и * как показано на доске
"""

for i in range(0, 5):
    for j in range(1, 6):
        if (j + i * 5) % 2 != 0:
            print(j + i * 5, end = '')
        else:
            print("*", end = '')
    print()
