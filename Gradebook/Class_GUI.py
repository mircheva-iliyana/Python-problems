import tkinter as tk
from tkinter import END
from tkinter.messagebox import showerror, showinfo
import tkinter.scrolledtext as st
import Common_Functions


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()

        # Define title and size
        self.title("Gradebook")
        self.geometry("800x600")

        # Define buttons
        self.button_add_student = tk.Button(self, text="Add Student", bg='green', command=self.add_student)
        self.button_remove_student = tk.Button(self, text="Remove Student", bg='orange', command=self.remove_student)
        self.button_add_subject = tk.Button(self, text="Add Subject", bg='green', command=self.add_subject_input)
        self.button_remove_subject = tk.Button(self, text="Remove Subject", bg='orange', command=self.remove_subject)
        self.button_add_grade = tk.Button(self, text="Add Grade", bg='green', command=self.add_grade)
        self.button_remove_grade = tk.Button(self, text="Remove Grade", bg='orange', command=self.remove_grade)
        self.button_show_all_students = tk.Button(self, text="Show all students", bg='pink', command=self.show_all_students)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back_input = tk.Button(self, text='Back', bg='grey', command=self.clear_input)
        self.button_modify = tk.Button(self, text="Modify Student Info", bg='blue', command=self.load_modify_buttons)
        self.button_hide_options = tk.Button(self, text='Hide options', bg='grey', command=self.hide_options)
        self.button_remove = tk.Button(self, text="Remove", bg='green',
                                       command=lambda: [Gradebook.remove_student(self.new_gradebook,
                                                                                 self.textbox_name.get()),
                                                        self.textbox_name.delete(0, END)])
        self.button_add_student_short = tk.Button(self, text="Add", bg='green',
                                                  command=lambda: [Gradebook.add_student(self.new_gradebook,
                                                                                         self.textbox_name.get(),
                                                                                         self.textbox_age.get(),
                                                                                         self.textbox_major.get()),
                                                                   self.textbox_name.delete(0, END),
                                                                   self.textbox_age.delete(0, END),
                                                                   self.textbox_major.delete(0, END)])
        self.button_add_subject_short = tk.Button(self, text='Add', bg='green',
                                                  command=lambda: [Gradebook.add_subject(
                                                      self.new_gradebook, self.textbox_name.get(),
                                                      self.textbox_subject.get()),
                                                                   self.textbox_name.delete(0, END),
                                                                   self.textbox_subject.delete(0, END)])

        self.button_remove_subject_short = tk.Button(self, text='Remove', bg='green',
                                                     command=lambda: [Gradebook.remove_subject(
                                                      self.new_gradebook, self.textbox_name.get(),
                                                      self.textbox_subject.get()),
                                                      self.textbox_name.delete(0, END),
                                                      self.textbox_subject.delete(0, END)])
        self.button_add_grade_short = tk.Button(self, text='Add', bg='green',
                                                command=lambda: [Gradebook.add_grade(self.new_gradebook,
                                                                                     self.textbox_name.get(),
                                                                                     self.textbox_subject.get(),
                                                                                     self.textbox_grade.get()),
                                                                 self.textbox_name.delete(0, END),
                                                                 self.textbox_subject.delete(0, END),
                                                                 self.textbox_grade.delete(0, END)])
        self.button_remove_grade_short = tk.Button(self, text='Remove', bg='orange',
                                                   command=lambda: [Gradebook.remove_grade(self.new_gradebook,
                                                                                           self.textbox_name.get(),
                                                                                           self.textbox_subject.get(),
                                                                                           self.textbox_grade.get()),
                                                                    self.textbox_name.delete(0, END),
                                                                    self.textbox_subject.delete(0, END),
                                                                    self.textbox_grade.delete(0, END)])

        # Define labels
        self.label_name = tk.Label(self, text='Name')
        self.label_age = tk.Label(self, text='Age')
        self.label_major = tk.Label(self, text='Major')
        self.label_subject = tk.Label(self, text='Subject')
        self.label_grade = tk.Label(self, text='Grade')

        # Define entries
        self.textbox_name = tk.Entry(self)
        self.textbox_age = tk.Entry(self)
        self.textbox_major = tk.Entry(self)
        self.textbox_subject = tk.Entry(self)
        self.textbox_grade = tk.Entry(self)

        # Define text area
        self.text_area = st.ScrolledText(self, width=60, height=10)

        # Create an instance of the Gradebook class
        self.new_gradebook = Gradebook()

    def add_student(self):
        self.name_input()
        self.label_age.grid(column=1, row=1)
        self.textbox_age.grid(column=2, row=1)
        self.label_major.grid(column=1, row=2)
        self.textbox_major.grid(column=2, row=2)
        self.button_add_student_short.grid(column=2, row=3)
        self.button_back.grid(column=3, row=3)

    def remove_student(self):
        self.name_input()
        self.button_remove.grid(column=2, row=3)
        self.button_back.grid(column=3, row=3)

    def add_subject_input(self):
        self.name_input()
        self.subject_input()
        self.button_add_subject_short.grid(column=2, row=2)
        self.button_back.grid(column=3, row=2)

    def remove_subject(self):
        self.name_input()
        self.subject_input()
        self.button_remove_subject_short.grid(column=2, row=2)
        self.button_back.grid(column=3, row=2)

    def add_grade(self):
        self.name_input()
        self.subject_input()
        self.label_grade.grid(column=1, row=2)
        self.textbox_grade.grid(column=2, row=2)
        self.button_add_grade_short.grid(column=2, row=3)
        self.button_back.grid(column=3, row=3)

    def remove_grade(self):
        self.name_input()
        self.subject_input()
        self.label_grade.grid(column=1, row=2)
        self.textbox_grade.grid(column=2, row=2)
        self.button_remove_grade_short.grid(column=2, row=3)
        self.button_back.grid(column=3, row=3)

    @staticmethod
    def generate_all_students(gradebook):
        return f'{gradebook}'

    def show_all_students(self):
        self.text_area.grid(column=5, row=4)
        self.button_back.grid(column=6, row=5)
        self.text_area.insert(END, self.generate_all_students(self.new_gradebook))

    def initialize_content(self):
        self.button_add_student.grid(column=0, row=0)
        self.button_remove_student.grid(column=0, row=1)
        self.button_modify.grid(column=0, row=2)
        self.button_show_all_students.grid(column=0, row=3)

    def name_input(self):
        self.label_name.grid(column=1, row=0)
        self.textbox_name.grid(column=2, row=0)
        self.textbox_name.focus()

    def subject_input(self):
        self.label_subject.grid(column=1, row=1)
        self.textbox_subject.grid(column=2, row=1)

    def back(self):
        Common_Functions.remove_fields(self.label_name, self.label_age, self.label_major, self.textbox_name,
                                       self.textbox_age, self.textbox_major, self.button_add_student_short,
                                       self.button_remove, self.label_subject, self.textbox_subject,
                                       self.button_add_subject_short, self.button_back, self.button_remove_subject_short,
                                       self.label_grade, self.textbox_grade, self.button_add_grade_short,
                                       self.button_remove_grade_short, self.text_area)

    def hide_options(self):
        Common_Functions.remove_fields(self.button_add_subject, self.button_remove_subject, self.button_add_grade,
                                       self.button_remove_grade, self.button_hide_options)

    def clear_input(self):
        Common_Functions.remove_fields(self.text_area)
        self.text_area.delete(1.0, END)

    def load_modify_buttons(self):
        self.button_add_subject.grid(column=1, row=4)
        self.button_remove_subject.grid(column=2, row=4)
        self.button_add_grade.grid(column=3, row=4)
        self.button_remove_grade.grid(column=4, row=4)
        self.button_hide_options.grid(column=5, row=5)

    @staticmethod
    def student_added_successfully():
        showinfo(title='Message', message='Student added')

    @staticmethod
    def student_already_exists():
        showerror(title='Message', message='Student already exists!')

    @staticmethod
    def invalid_name():
        showerror(title='Message', message='Please, enter a valid name')

    @staticmethod
    def invalid_subject():
        showerror(title='Message', message='Please, enter a valid subject')

    @staticmethod
    def student_deleted():
        showinfo(title='Message', message='Student deleted')

    @staticmethod
    def student_does_not_exist():
        showerror(title='Message', message='Student does not exist')

    @staticmethod
    def subject_already_added():
        showerror(title='Message', message='Subjects is already added')

    @staticmethod
    def subject_added_successfully():
        showinfo(title='Message', message='Subject added successfully')

    @staticmethod
    def subject_removed():
        showinfo(title='Message', message='Subject removed')

    @staticmethod
    def subject_does_not_exist():
        showerror(title='Message', message='Subject does not exist')

    @staticmethod
    def grade_added():
        showinfo(title='Message', message='Grade added successfully')

    @staticmethod
    def grade_not_valid():
        showerror(title='Message', message='Please enter a valid grade')

    @staticmethod
    def grade_not_present():
        showerror(title='Message', message='This grade is not in the record')

    @staticmethod
    def grade_removed():
        showinfo(title='Message', message='Grade removed')


from Class_Gradebook import Gradebook
