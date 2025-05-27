#!/usr/bin/python3
"""Module abc class"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """animal abstract class"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """subclass dog"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """subclass cat"""
    def sound(self):
        return "Meow"
