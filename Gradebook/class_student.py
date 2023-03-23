class Student:

    def __init__(self, name, age, major, subjects={}):
        self.name = name
        self.age = age
        self.major = major
        self.subjects = subjects

    def __str__(self):
        return f'{self.name}, {self.age}, {self.major}, {self.subjects}'
