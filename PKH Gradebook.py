# Create a virtual gradebook that contains all students' grades for all subjects.
# The virtual gradebook should provide functionality to add a new student,
# add grades for a student, modify grades of a student, add a subject and everything else you can think of :P


gradebook = {}


def add_student(name):
    try:
        gradebook[name] = {}
    except KeyError:
        print("This student already exists")


def add_subject(name, subject):
    try:
        gradebook[name][subject] = []
    except KeyError:
        print(f'There is no {name} in the gradebook')


def add_grades(name, subject, grades):
    try:
        for i in grades:
            gradebook[name][subject].append(i)
    except KeyError:
        print(f'There is no {name} or {subject} in the gradebook')


def modify_grades(name, subject, new_grades):
    try:
        gradebook[name][subject] = new_grades
    except KeyError:
        print(f'There is no {name} or {subject} in the gradebook')


add_student('Iliyana')
add_subject('Iliyana', 'Chemistry')
add_grades('Iliyana', 'Chemistry', [6, 5])
add_grades('Iliyana', 'English', [6, 5])
modify_grades('Iliyana', 'Chemistry', [6, 6])

add_student('Boyko')
add_subject('Boyk', 'Literature')
add_subject('Boyko', 'Literature')
add_grades('Boyko', 'Literature', [5, 5])

print(gradebook)


