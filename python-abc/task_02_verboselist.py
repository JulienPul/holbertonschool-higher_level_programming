#!/usr/bin/python3
"""Module 2:verboselist """


from typing import List
from abc import ABC, abstractmethod
	

class VerboseList(list, ABC):

    @abstractmethod
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    @abstractmethod
    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    @abstractmethod
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    @abstractmethod
    def pop(self, index=-1):
        item = self[index]if -len(self) <= index < len(self)else None
        result = super().pop(index)
        print(f"Popped [{result}] from the list.")
        return result
