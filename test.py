import os
from typing import Callable


def hayashi(x,y):
    return x+y


def kaneki(x,y):
    return x-y

def hayashi_kaneki(x,y):
    return 0


class Nlist(list):
    def map(self, func:Callable):
        return map(lambda x: func(x), self)
