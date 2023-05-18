"""
Используя паттерн Bridge, реализовать объект «множество», которое представляется различными структурами данных в
зависимости от числа элементов. При этом «множество» должно уметь изменять внутреннюю структуру в зависимости от
фактического количества объектов. Обязательно реализовать методы добавления, удаления и поиска объекта в множестве
по значению.
"""

import collections
from abc import ABC, abstractmethod


class AbstractRelease(ABC):
    """
    Абстрактный класс для реализации внутренних структур данных
    """

    @abstractmethod
    def add(self, el):
        """Добавить элемент в множество"""
        pass

    @abstractmethod
    def remove(self, el):
        """Удалить элемент из множества"""
        pass

    @abstractmethod
    def find(self, el):
        """Найти элемент в множестве"""
        pass


class ReleaseOne(AbstractRelease):
    """
    Конкретная реализация множества с использованием deque и list
    """

    def __init__(self):
        self.arr = collections.deque()

    def change(self):
        if len(self.arr) < 3:
            if self.arr is not collections.deque:
                cur = collections.deque()
                for el in self.arr:
                    cur.append(el)
                self.arr = cur
        else:
            if self.arr is not list:
                cur = []
                for el in self.arr:
                    cur.append(el)
                self.arr = cur

    def add(self, el):
        self.arr.append(el)
        self.change()

    def remove(self, el):
        if el not in self.arr:
            print("Not found")
            return 1
        self.arr.remove(el)
        self.change()

    def find(self, el):
        if el not in self.arr:
            return "Not found"
        return self.arr.index(el)


class ReleaseTwo(AbstractRelease):
    """
    Конкретная реализация множества с использованием tuple и list
    """
    def __init__(self):
        self.arr = tuple()

    def change(self):
        if len(self.arr) < 3:
            if self.arr is not tuple:
                cur = tuple()
                for el in self.arr:
                    cur += tuple([el])
                self.arr = cur
        else:
            if self.arr is not list:
                cur = []
                for el in self.arr:
                    cur.append(el)
                self.arr = cur

    def add(self, el):
        if type(self.arr) is tuple:
            self.arr += tuple([el])
        else:
            self.arr.append(el)
        self.change()

    def remove(self, el):
        if el not in self.arr:
            print("Not found")
            return 1
        if self.arr is tuple:
            self.arr = tuple(list(self.arr).remove(el))
        else:
            self.arr.remove(el)
        self.change()

    def find(self, el):
        if el not in self.arr:
            return "Not found"
        return self.arr.index(el)


class Abstraction:
    def __init__(self, release: AbstractRelease):
        self.release = release

    def add(self, el):
        self.release.add(el)

    def remove(self, el):
        self.release.remove(el)

    def find(self, el):
        return self.release.find(el)


s = Abstraction(ReleaseTwo())

for i in range(0, 7, 2):
    s.add(i)
    print(s.release.arr)
print(s.find(2))
s.remove(2)
s.remove(4)
print(s.release.arr)
