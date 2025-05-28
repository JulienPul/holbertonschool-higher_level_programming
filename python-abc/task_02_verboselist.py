#!/usr/bin/python3
"""Module 2:verboselist """


from typing import List
from abc import ABC, abstractmethod
	

class VerboseList(list, ABC):

    @abstractmethod
    def append(self, item):
        super().append(item)
        return print("“Added {} to the list.”", (item))

    @abstractmethod
    def extend(self, items):
        super().extend(items)
        return ("“Extended the list with [x] items.”")

    @abstractmethod
    def remove(self, item):
        super().remove(item)
        return ("“Removed {} from the list.”", (item))

    @abstractmethod
    def pop(self, index=-1):
        super().pop(index)
        return ("“Popped {} from the list.”", (index))
