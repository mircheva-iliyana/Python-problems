from class_student import Student
from class_messages import Messages


class Gradebook:

    def __init__(self):
        self.gradebook = {}

    def __str__(self):
        for student in self.gradebook:
            return f'{student} -> {self.gradebook[student]}'

    def add_student(self, name, age, major):
        if name in self.gradebook:
            return Messages.STUDENT_ALREADY_EXISTS
        elif name == '':
            return Messages.INVALID_NAME
        elif age == '':
            return Messages.AGE_NOT_ADDED
        elif major == '':
            return Messages.MAJOR_NOT_ADDED
        else:
            self.gradebook[name] = Student(name, age, major)
            return Messages.STUDENT_ADDED_SUCCESSFULLY

    def remove_student(self, name):
        if name in self.gradebook:
            del self.gradebook[name]
            return Messages.STUDENT_DELETED
        elif name == '':
            return Messages.INVALID_NAME
        else:
            return Messages.STUDENT_DOES_NOT_EXIST

    def add_subject(self, name, subject):
        if name == '':
            return Messages.INVALID_NAME
        if subject == '':
            return Messages.INVALID_SUBJECT
        if name in self.gradebook:
            if subject not in self.gradebook[name].subjects:
                self.gradebook[name].subjects[subject] = []
                return Messages.SUBJECT_ADDED_SUCCESSFULLY
            else:
                return Messages.SUBJECT_ALREADY_ADDED
        else:
            return Messages.STUDENT_DOES_NOT_EXIST

    def remove_subject(self, name, subject):
        if name in self.gradebook:
            if subject in self.gradebook[name].subjects:
                del self.gradebook[name].subjects[subject]
                return Messages.SUBJECT_REMOVED
            else:
                return Messages.SUBJECT_DOES_NOT_EXIST
        elif name == '':
            return Messages.INVALID_NAME
        elif subject == '':
            return Messages.INVALID_SUBJECT
        else:
            return Messages.STUDENT_DOES_NOT_EXIST

    def add_grade(self, name, subject, new_grade):
        if name in self.gradebook:
            if subject in self.gradebook[name].subjects:
                if new_grade != '':
                    if 2 <= int(new_grade) <= 6:
                        self.gradebook[name].subjects[subject].append(new_grade)
                        return Messages.GRADE_ADDED
                    else:
                        return Messages.GRADE_NOT_VALID
                else:
                    return Messages.GRADE_NOT_VALID
            else:
                return Messages.SUBJECT_DOES_NOT_EXIST
        elif name == '':
            return Messages.INVALID_NAME
        elif subject == '':
            return Messages.INVALID_SUBJECT
        else:
            return Messages.STUDENT_DOES_NOT_EXIST

    def remove_grade(self, name, subject, grade):
        if name in self.gradebook:
            if subject in self.gradebook[name].subjects:
                if grade in self.gradebook[name].subjects[subject]:
                    if 2 <= int(grade) <= 6:
                        self.gradebook[name].subjects[subject].remove(grade)
                        return Messages.GRADE_REMOVED
                    else:
                        return Messages.GRADE_NOT_VALID
                else:
                    return Messages.GRADE_NOT_PRESENT
            else:
                return Messages.SUBJECT_DOES_NOT_EXIST
        elif name == '':
            return Messages.INVALID_NAME
        elif subject == '':
            return Messages.INVALID_SUBJECT
        else:
            return Messages.STUDENT_DOES_NOT_EXIST
