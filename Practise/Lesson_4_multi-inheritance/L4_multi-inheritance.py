
class Human:

    def __init__(self, age, nationality):
        self.age = age
        self.nationality = nationality

    def show_age(self):
        return self.age

    def make_older(self):
        self.age += 1

class Student:

    def __init__(self, field_of_studies, subjects):
        self.field_of_studies = field_of_studies
        self.subjects = subjects

    def show_all_subjects(self):
        for i in self.subjects:
            print(f"Subject: {i}")

class Sportsman:

    def __init__(self, disicipline):
        self.discipline = disicipline

    def do_training(self):
        print(f"I'm doing {self.discipline} trainig.")

class AWF_student(Human, Student, Sportsman):

    def __init__(self, age, nationality, field_of_studies, subjects, disicipline):
        Human.__init__(self, age, nationality)
        Student.__init__(self, field_of_studies, subjects)
        Sportsman.__init__(self, disicipline)


Edward = AWF_student(24, 'Poland', 'Sport', ['Psychology', 'Anatomy', 'Engineering and Chemistry'], 'football')

print('FROM HUMAN CLASS')
print(Edward.show_age())
Edward.make_older()
print(Edward.show_age())
print('FROM STUDENT CLASS')
Edward.show_all_subjects()
print('FROM SPORTSMAN CLASS')
Edward.do_training()