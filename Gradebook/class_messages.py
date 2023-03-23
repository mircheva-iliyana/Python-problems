from enum import Enum
from tkinter.messagebox import showerror, showinfo


class Messages(Enum):
    STUDENT_ADDED_SUCCESSFULLY = 'Student added'
    STUDENT_ALREADY_EXISTS = 'Student already exists!'
    INVALID_NAME = 'Please, enter a valid name'
    INVALID_SUBJECT = 'Please, enter a valid subject'
    STUDENT_DELETED = 'Student deleted'
    STUDENT_DOES_NOT_EXIST = 'Student does not exist'
    SUBJECT_ALREADY_ADDED = 'Subjects is already added'
    SUBJECT_ADDED_SUCCESSFULLY = 'Subject added successfully'
    SUBJECT_REMOVED = 'Subject removed'
    SUBJECT_DOES_NOT_EXIST = 'Subject does not exist'
    GRADE_ADDED = 'Grade added successfully'
    GRADE_NOT_VALID = 'Please enter a valid grade'
    GRADE_NOT_PRESENT = 'This grade is not in the record'
    GRADE_REMOVED = 'Grade removed'
    AGE_NOT_ADDED = 'Add a valid age'
    MAJOR_NOT_ADDED = 'Add a major'

    def show_info(self):
        showinfo(title='Message', message=self.value)
