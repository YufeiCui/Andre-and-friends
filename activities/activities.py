from enum import Enum


class Activity(object):

    def __init__(self, title: str, length: float, fun: bool):
        self._title = title
        self._length = length
        self._fun = fun

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self.title = title

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self.length = length

    @property
    def fun(self):
        return self._fun

    @fun.setter
    def fun(self, fun):
        self.fun = fun


class Computer(Activity):

    def __init__(self, title="Computer Time", length=0.5):
        Activity.__init__(self, title, length, False)


class DS(Activity):

    def __init__(self, title="Playing the DS", length=0.5):
        Activity.__init__(self, title, length, False)


class TV(Activity):

    def __init__(self, title="Watching TV", length=0.5):
        Activity.__init__(self, title, length, False)


class Lecture(Activity):

    def __init__(self, title="Watch Lecture", length=1):
        Activity.__init__(self, title, length, False)


class Homework(Activity):

    def __init__(self, title="Do Work Report", length=1):
        Activity.__init__(self, title, length, False)


class Read(Activity):

    def __init__(self, title="Read Kindle", length=1):
        Activity.__init__(self, title, length, False)


class Activities(Enum):
    COMPUTER = Computer()
    DS = DS(title="Play Pokemon Ultra Sun!")
    TV = TV(title="Watch YouTube")
    LECTURE = Lecture(title="Watch CSCC73 and take notes")
    REPORT = Homework(title="Do Co-op Work Term Report")
    READ = Read(title="Read the Phoenix Project and then move onto Ready Player One")
