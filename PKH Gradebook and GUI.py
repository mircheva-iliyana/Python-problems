import tkinter as tk
from tkinter import messagebox
# Changed

class Student:

    def __init__(self, name, age, major, courses, grades):
        self.name = name
        self.age = age
        self.major = major
        self.courses = courses
        self.grades = grades

    def add_grades(self, new_grades):
        for grade in new_grades:
            self.grades.append(grade)

    def __str__(self):
        return f'Major: {self.major}'


class Gradebook:

    def __init__(self):
        self.gradebook = {}

    def show_all_students(self):
        for key, item in self.gradebook.items():
            print(f'{self.gradebook[key]} - {self.gradebook[item]}')

    def add_student(self):
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        major = input("Enter student major: ")
        courses = input("Enter student courses (separated by commas): ")
        grades = input("Enter student grades (separated by commas): ")

        courses = courses.split(",")
        grades = [int(grade) for grade in grades.split(",")]

        if name not in self.gradebook:
            student = Student(name, age, major, courses, grades)
            self.gradebook[name] = student
            messagebox.showinfo(f"Added student {name}")
        else:
            messagebox.showinfo(f"Student {name} already exists in gradebook")

    def remove_student(self):
        name = input("Enter student name: ")
        if name in self.gradebook:
            del self.gradebook[name]
            print(f"Removed student {name}")
        else:
            print(f"Student {name} not found in gradebook")

    def add_subject(self):
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        if name in self.gradebook:
            self.gradebook[name].courses.append(subject)
            print(f"Added subject {subject} to student {name}")
        else:
            print(f"Student {name} not found in gradebook")

    def remove_subject(self):
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        if name in self.gradebook and subject in self.gradebook[name].courses:
            self.gradebook[name].courses.remove(subject)
            print(f"Removed subject {subject} from student {name}")
        else:
            print(f"Student {name} not found in gradebook or subject {subject} not found in student's courses")


gradebook = Gradebook()

root = tk.Tk()
root.title("Gradebook")
root.geometry("400x300")
label = tk.Label(root, text="Gradebook")
label.pack()


button_add_student = tk.Button(root, text="Add Student", command=gradebook.add_student)
button_add_student.pack()

button_remove_student = tk.Button(root, text="Remove Student", command=gradebook.remove_student)
button_remove_student.pack()

button_add_subject = tk.Button(root, text="Add Subject", command=gradebook.add_subject)
button_add_subject.pack()

button_remove_subject = tk.Button(root, text="Remove Subject", command=gradebook.remove_subject)
button_remove_subject.pack()

button_remove_subject = tk.Button(root, text="Show all students", command=gradebook.show_all_students)
button_remove_subject.pack()

root.mainloop()
