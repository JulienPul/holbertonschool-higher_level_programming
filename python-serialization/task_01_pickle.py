#!/usr/bin/env python3
"""Module 1"""
import pickle

class CustomObject:
    """ class named CustomObject"""

    def __init__(self, name, age, is_student):
        """name (a string)age (an integer)
        is_student (a boolean)"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print out the object’s attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize the current instance of the object"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """oad and return an instance of the CustomObject"""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception) as e:
            print(f"Deserialization error: {e}")
            return None
