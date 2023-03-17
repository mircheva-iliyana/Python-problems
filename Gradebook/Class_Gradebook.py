from Class_GUI import GUI


class Gradebook:

    def __init__(self):
        self.gradebook = {}

    def __str__(self):
        return f'{self.gradebook}'

    def add_student(self, name, age, major):
        if name in self.gradebook:
            GUI.student_already_exists()
        elif name == '':
            GUI.invalid_name()
        else:
            self.gradebook[name] = Student(name, age, major)
            GUI.student_added_successfully()

    def remove_student(self, name):
        if name in self.gradebook:
            del self.gradebook[name]
            GUI.student_deleted()
        elif name == '':
            GUI.invalid_name()
        else:
            GUI.student_does_not_exist()

    def add_subject(self, name, subject):
        if name in self.gradebook:
            if subject not in self.gradebook[name].subjects:
                self.gradebook[name].subjects[subject] = []
                GUI.subject_added_successfully()
            else:
                GUI.subject_already_added()
        elif name == '':
            GUI.invalid_name()
        elif subject == '':
            GUI.invalid_subject()
        else:
            GUI.student_does_not_exist()

    def remove_subject(self, name, subject):
        if name in self.gradebook:
            if subject in self.gradebook[name].subjects:
                del self.gradebook[name].subjects[subject]
                GUI.subject_removed()
            else:
                GUI.subject_does_not_exist()
        elif name == '':
            GUI.invalid_name()
        elif subject == '':
            GUI.invalid_subject()
        else:
            GUI.student_does_not_exist()

    def add_grade(self, name, subject, new_grade):
        if name in self.gradebook:
            if subject in self.gradebook[name].subjects:
                if 2 <= int(new_grade) <= 6:
                    self.gradebook[name].subjects[subject].append(new_grade)
                    GUI.grade_added()
                else:
                    GUI.grade_not_valid()
            else:
                GUI.subject_does_not_exist()
        elif name == '':
            GUI.invalid_name()
        elif subject == '':
            GUI.invalid_subject()
        else:
            GUI.student_does_not_exist()

    def remove_grade(self, name, subject, grade):
        if name in self.gradebook:
            if subject in self.gradebook[name].subjects:
                if grade in self.gradebook[name].subjects[subject]:
                    if 2 <= int(grade) <= 6:
                        self.gradebook[name].subjects[subject].remove(grade)
                        GUI.grade_removed()
                    else:
                        GUI.grade_not_valid()
                else:
                    GUI.grade_not_present()
            else:
                GUI.subject_does_not_exist()
        elif name == '':
            GUI.invalid_name()
        elif subject == '':
            GUI.invalid_subject()
        else:
            GUI.student_does_not_exist()


from Class_Student import Student
