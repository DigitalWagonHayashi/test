import os
from typing import Callable


def hayashi(x,y):
    return x+y


def kaneki(x,y):
    return x-y


class Nlist(list):
    def map(self, func:Callable):
        return map(lambda x: func(x), self)
