class Student:
    items = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0
        Student.items.append(self)

    def score_lecturer(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def average_score_student(self):
        list_score_st = []
        for cours in self.grades:
            for grade in self.grades[cours]:
                list_score_st += [grade]
        if not list_score_st:
            return 'Ошибка!'
        else:
            average = sum(list_score_st) / len(list_score_st)
        return average


    def __lt__(self, other):
        return self.average < other.average

    def __gt__(self, other):
        return self.average > other.average

    def __eq__(self, other):
        return self.average == other.average

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{round(self.average_score_student(), 2)}\nКурсы в процессе изучения:{self.courses_in_progress}\n' \
               f'Завершенные курсы:{self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    items = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average = 0
        Lecturer.items.append(self)

    def average_score_lecturer(self):
        list_score_lec = []
        for cours in self.grades:
            for grade in self.grades[cours]:
                list_score_lec += [grade]
        if not list_score_lec:
            return 'Ошибка!'
        else:
            average = sum(list_score_lec) / len(list_score_lec)
        return average

    def __lt__(self, other):
        return self.average < other.average

    def __gt__(self, other):
        return self.average > other.average

    def __eq__(self, other):
        return self.average == other.average

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:' \
            f' {round(self.average_score_lecturer(), 2)}'

class Reviewer(Mentor):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student1 = Student('Roboute', 'Guilliman', 'Male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student2 = Student('Cyrene', 'Valentien ', 'Female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']

mentor1 = Reviewer('Malcador', 'Sigillite')
mentor1.courses_attached += ['Python']

mentor2 = Reviewer('Belisarius ', 'Cawl ')
mentor2.courses_attached += ['Git']

mentor3 = Lecturer('Lorgar', 'Aurelian')
mentor3.courses_attached += ['Python']

mentor4 = Lecturer('Horus', 'Lupercal')
mentor4.courses_attached += ['Git']

mentor1.rate_st(student1, 'Python', 3)
mentor1.rate_st(student2, 'Python', 10)

mentor2.rate_st(student1, 'Git', 4)
mentor2.rate_st(student2, 'Git', 6)

student1.score_lecturer(mentor3, 'Python', 10)
student1.score_lecturer(mentor4, 'Git', 6)
student1.finished_courses += ['Blender']

student2.score_lecturer(mentor3, 'Python', 8)
student2.score_lecturer(mentor4, 'Git', 10)
student2.finished_courses += ['3dMAX']

list_students = Student.items
def average_rating_st(list_students, course):
    list_grades = []
    for student in list_students:
        if course in student.grades:
            list_grades += student.grades[course]
    if not list_grades:
        return 'Ошибка!'
    else:
        result = sum(list_grades) / len(list_grades)
        return result


list_lecturers = Lecturer.items
def average_rating_lec(list_lecturers, course):
    list_grades = []
    for lecturer in list_lecturers:
        if course in lecturer.grades:
            list_grades += lecturer.grades[course]
    if not list_grades:
        return 'Ошибка!'
    else:
        result = sum(list_grades) / len(list_grades)
        return result
print("************")
print(f'\nСписок студентов:\n{student1}\n\n{student2}\n')
print("************")
print(f'\nСписок лекторов:\n{mentor1}\n\n{mentor2}\n\n{mentor3}\n\n{mentor4}\n')
print("************")
print(f'\nСравнение оценок студентов по срденему значению: '
      f'\n (lt) {student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1.__lt__(student2)}\n' \
      f'\n (gt) {student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1.__gt__(student2)}\n' \
      f'\n (eq) {student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1.__eq__(student2)}\n')
print("************")
print(f'Сравнение оценок  лекторовпо срденему значению: '
      f'\n (lt) {mentor3.name} {mentor3.surname} < {mentor4.name} {mentor4.surname} = {mentor3.__lt__(mentor4)}\n' \
      f'\n (gt) {mentor3.name} {mentor3.surname} < {mentor4.name} {mentor4.surname} = {mentor3.__gt__(mentor4)}\n' \
      f'\n (eq) {mentor3.name} {mentor3.surname} < {mentor4.name} {mentor4.surname} = {mentor3.__eq__(mentor4)}\n')
print("************")

print(f"\nСредняя оценка студентов за курс {'Python'}: {average_rating_st(list_students, 'Python')}")
print(f"\nСредняя оценка студентов за курс {'Git'}: {average_rating_st(list_students, 'Git')}")
print(f"\nСредняя оценка лекторов за курс {'Python'}: {average_rating_lec(list_lecturers, 'Python')}")
print(f"\nСредняя оценка лекторов за курс {'Git'}: {average_rating_lec(list_lecturers, 'Git')}")