"""
Реализовать класс словаря,
если неверный ключ то выведет значение (get, getitem)

"""

class MyDict(dict):
    """ Класс расширяющий функционал dict - при вводе некорректного ключа выведет -1 """
    def __getitem__(self, key):
        if self.get(key) is None:
            return -1
        return super().__getitem__(key)


dic = MyDict({3: "344"})
print(dic[0])
