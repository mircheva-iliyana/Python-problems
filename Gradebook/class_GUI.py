import tkinter as tk
from tkinter import END
import tkinter.scrolledtext as st
import common_functions
from class_gradebook import Gradebook
from class_messages import Messages


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()

        # Define title and size
        self.title("Gradebook")
        self.geometry("800x600")

        # Define buttons
        self.button_add_student = tk.Button(self)
        self.button_remove_student = tk.Button(self)
        self.button_modify = tk.Button(self)
        self.button_show_all_students = tk.Button(self)
        self.button_add_subject = tk.Button(self)
        self.button_remove_subject = tk.Button(self)
        self.button_add_grade = tk.Button(self)
        self.button_remove_grade = tk.Button(self)
        self.button_hide_options = tk.Button(self)
        self.button_back = tk.Button(self)
        self.button_back_input = tk.Button(self)
        self.button_remove = tk.Button(self)
        self.button_add_student_short = tk.Button(self)
        self.button_add_subject_short = tk.Button(self)
        self.button_remove_subject_short = tk.Button(self)
        self.button_add_grade_short = tk.Button(self)
        self.button_remove_grade_short = tk.Button(self)

        # Define labels
        self.label_name = tk.Label(self)
        self.label_subject = tk.Label(self)
        self.label_age = tk.Label(self)
        self.label_major = tk.Label(self)
        self.label_grade = tk.Label(self)

        # Define Entries
        self.textbox_name = tk.Entry(self)
        self.textbox_subject = tk.Entry(self)
        self.textbox_age = tk.Entry(self)
        self.textbox_major = tk.Entry(self)
        self.textbox_grade = tk.Entry(self)

        # Define text area
        self.text_area = st.ScrolledText(self, width=60, height=10)

        # Create an instance of the Gradebook class
        self.new_gradebook = None

    def setup(self):
        """ Instantiates an object from Gradebook class """
        self.new_gradebook = Gradebook()

    def load_initial_content(self):
        """Display the initial buttons on the screen"""
        self.button_add_student = tk.Button(self, text="Add Student", bg='green',
                                            command=self.load_add_student_fields)
        self.button_remove_student = tk.Button(self, text="Remove Student", bg='orange',
                                               command=self.load_remove_student_fields)
        self.button_modify = tk.Button(self, text="Modify Student Info", bg='blue', command=self.load_modify_buttons)
        self.button_show_all_students = tk.Button(self, text="Show all students", bg='pink',
                                                  command=self.show_all_students)
        self.button_add_student.grid(column=0, row=0)
        self.button_remove_student.grid(column=0, row=1)
        self.button_modify.grid(column=0, row=2)
        self.button_show_all_students.grid(column=0, row=3)

    def load_add_student_fields(self):
        """Displays the additional fields and buttons for adding a student"""
        self.load_name_input()
        self.load_age_and_major_input()
        self.button_add_student_short = tk.Button(self, text="Add", bg='green',
                                                  command=lambda: [self.add_student(),
                                                                   self.textbox_name.delete(0, END),
                                                                   self.textbox_age.delete(0, END),
                                                                   self.textbox_major.delete(0, END)])
        self.button_add_student_short.grid(column=2, row=3)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=3, row=3)

    def load_remove_student_fields(self):
        """Displays the additional fields and buttons for removing a student"""
        self.load_name_input()
        self.button_remove = tk.Button(self, text="Remove", bg='green',
                                       command=lambda: [self.remove_student(),
                                                        self.textbox_name.delete(0, END)])
        self.button_remove.grid(column=2, row=3)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=3, row=3)

    def load_modify_buttons(self):
        """Displays the additional fields and buttons for modifying a student"""
        self.button_add_subject = tk.Button(self, text="Add Subject", bg='green', command=self.add_subject_input)
        self.button_remove_subject = tk.Button(self, text="Remove Subject", bg='orange',
                                               command=self.remove_subject_input)
        self.button_add_grade = tk.Button(self, text="Add Grade", bg='green', command=self.add_grade_input)
        self.button_remove_grade = tk.Button(self, text="Remove Grade", bg='orange', command=self.remove_grade_input)
        self.button_hide_options = tk.Button(self, text='Hide options', bg='grey', command=self.hide_options)
        self.button_add_subject.grid(column=1, row=4)
        self.button_remove_subject.grid(column=2, row=4)
        self.button_add_grade.grid(column=3, row=4)
        self.button_remove_grade.grid(column=4, row=4)
        self.button_hide_options.grid(column=5, row=5)

    def load_name_input(self):
        """Load input field and label for name input"""
        self.label_name = tk.Label(self, text='Name')
        self.textbox_name = tk.Entry(self)
        self.label_name.grid(column=1, row=0)
        self.textbox_name.grid(column=2, row=0)
        self.textbox_name.focus()

    def load_subject_input(self):
        """Load input field and label for subject input"""
        self.label_subject = tk.Label(self, text='Subject')
        self.textbox_subject = tk.Entry(self)
        self.label_subject.grid(column=1, row=1)
        self.textbox_subject.grid(column=2, row=1)

    def load_age_and_major_input(self):
        """Load input fields and labels for age and major input"""
        self.label_age = tk.Label(self, text='Age')
        self.label_major = tk.Label(self, text='Major')
        self.textbox_age = tk.Entry(self)
        self.textbox_major = tk.Entry(self)
        self.label_age.grid(column=1, row=1)
        self.textbox_age.grid(column=2, row=1)
        self.label_major.grid(column=1, row=2)
        self.textbox_major.grid(column=2, row=2)

    def load_grade_input(self):
        """Load input field and label for grade input"""
        self.label_grade = tk.Label(self, text='Grade')
        self.textbox_grade = tk.Entry(self)
        self.label_grade.grid(column=1, row=2)
        self.textbox_grade.grid(column=2, row=2)

    def add_subject_input(self):
        """Load input fields for adding a subject"""
        self.load_name_input()
        self.load_subject_input()
        self.button_add_subject_short = tk.Button(self, text='Add', bg='green',
                                                  command=lambda: [self.add_subject(),
                                                                   self.textbox_name.delete(0, END),
                                                                   self.textbox_subject.delete(0, END)])
        self.button_add_subject_short.grid(column=2, row=2)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=3, row=2)

    def remove_subject_input(self):
        """Load input fields for removing a subject"""
        self.load_name_input()
        self.load_subject_input()
        self.button_remove_subject_short = tk.Button(self, text='Remove', bg='green',
                                                     command=lambda: [self.remove_subject(),
                                                                      self.textbox_name.delete(0, END),
                                                                      self.textbox_subject.delete(0, END)])
        self.button_remove_subject_short.grid(column=2, row=2)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=3, row=2)

    def add_grade_input(self):
        """Load input fields for adding a grade"""
        self.load_name_input()
        self.load_subject_input()
        self.load_grade_input()
        self.button_add_grade_short = tk.Button(self, text='Add', bg='green',
                                                command=lambda: [self.add_grade(),
                                                                 self.textbox_name.delete(0, END),
                                                                 self.textbox_subject.delete(0, END),
                                                                 self.textbox_grade.delete(0, END)])
        self.button_add_grade_short.grid(column=2, row=3)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=3, row=3)

    def remove_grade_input(self):
        """Load input fields for removing a grade"""
        self.load_name_input()
        self.load_subject_input()
        self.load_grade_input()
        self.button_remove_grade_short = tk.Button(self, text='Remove', bg='orange',
                                                   command=lambda: [self.remove_grade(),
                                                                    self.textbox_name.delete(0, END),
                                                                    self.textbox_subject.delete(0, END),
                                                                    self.textbox_grade.delete(0, END)])
        self.button_remove_grade_short.grid(column=2, row=3)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=3, row=3)

    def add_student(self):
        """Adds a new student to the Gradebook"""
        name = self.textbox_name.get()
        age = self.textbox_age.get()
        major = self.textbox_major.get()
        result = self.new_gradebook.add_student(name, age, major)
        Messages.show_info(result)

    def remove_student(self):
        """Removes a new student from the Gradebook"""
        name = self.textbox_name.get()
        result = self.new_gradebook.remove_student(name)
        Messages.show_info(result)

    def add_subject(self):
        """Adds a new subject to a student in the Gradebook"""
        name = self.textbox_name.get()
        subject = self.textbox_subject.get()
        result = self.new_gradebook.add_subject(name, subject)
        Messages.show_info(result)

    def remove_subject(self):
        """Removes a subject from a student in the Gradebook"""
        name = self.textbox_name.get()
        subject = self.textbox_subject.get()
        result = self.new_gradebook.remove_subject(name, subject)
        Messages.show_info(result)

    def add_grade(self):
        """Adds a new grade to a student's subject in the Gradebook"""
        name = self.textbox_name.get()
        subject = self.textbox_subject.get()
        new_grade = self.textbox_grade.get()
        result = self.new_gradebook.add_grade(name, subject, new_grade)
        Messages.show_info(result)

    def remove_grade(self):
        """Removes grade from a student's subject in the Gradebook"""
        name = self.textbox_name.get()
        subject = self.textbox_subject.get()
        grade = self.textbox_grade.get()
        result = self.new_gradebook.remove_grade(name, subject, grade)
        Messages.show_info(result)

    def show_all_students(self):
        """Generates a field with all the students in the Gradebook and their attributes"""
        self.text_area.grid(column=5, row=4)
        self.button_back = tk.Button(self, text="Back", bg='grey', command=self.back)
        self.button_back.grid(column=6, row=5)
        self.button_back_input = tk.Button(self, text='Back', bg='grey', command=self.clear_input)
        self.text_area.insert(END, f'{self.new_gradebook}')

    def back(self):
        """A function for the back button to remove all the widgets and go back to home page"""
        common_functions.remove_fields(self.button_remove, self.button_add_student_short, self.button_add_subject_short,
                                       self.button_remove_subject_short, self.button_add_grade_short,
                                       self.button_remove_grade_short, self.label_name, self.label_subject,
                                       self.label_age, self.label_major, self.label_grade, self.textbox_name,
                                       self.textbox_subject, self.textbox_age, self.textbox_major, self.textbox_grade,
                                       self.text_area, self.button_back)

    def hide_options(self):
        """A function for the hide button to remove all the widgets and go back to home page"""
        common_functions.remove_fields(self.button_add_subject, self.button_remove_subject, self.button_add_grade,
                                       self.button_remove_grade, self.button_hide_options)

    def clear_input(self):  # not working properly
        common_functions.remove_fields(self.text_area)
        self.text_area.delete(1.0, END)


app = GUI()
app.load_initial_content()
app.setup()
app.mainloop()
