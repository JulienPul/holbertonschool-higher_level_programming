#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class Student that defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
