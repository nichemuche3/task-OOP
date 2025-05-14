class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and 
            course in lecturer.courses_attached and 
            (course in self.courses_in_progress or course in self.finished_courses) and 
            1 <= grade <= 10):
            
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка: Невозможно поставить оценку"

    def __str__(self):
        avg_grade = self._get_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет курсов"
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _get_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() < other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() == other._get_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._get_avg_grade()
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def _get_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() < other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() == other._get_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calculate_avg_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if not total_grades:
        return 0
    return round(sum(total_grades) / len(total_grades), 1)

def calculate_avg_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if not total_grades:
        return 0
    return round(sum(total_grades) / len(total_grades), 1)


student1 = Student("Иван", "Иванов", "мужской")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]
student1.grades = {"Python": [9, 10, 8], "Git": [8, 9]}

student2 = Student("Мария", "Петрова", "женский")
student2.courses_in_progress = ["Python", "JavaScript"]
student2.finished_courses = ["Основы программирования"]
student2.grades = {"Python": [10, 9, 10], "JavaScript": [8, 9]}

lecturer1 = Lecturer("Алексей", "Смирнов")
lecturer1.courses_attached = ["Python", "Git"]
lecturer1.grades = {"Python": [9, 10, 8], "Git": [8, 9]}

lecturer2 = Lecturer("Ольга", "Кузнецова")
lecturer2.courses_attached = ["Python", "JavaScript"]
lecturer2.grades = {"Python": [10, 9, 10], "JavaScript": [9, 8]}

reviewer1 = Reviewer("Дмитрий", "Васильев")
reviewer1.courses_attached = ["Python", "Git"]

reviewer2 = Reviewer("Елена", "Соколова")
reviewer2.courses_attached = ["JavaScript", "Python"]

reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Git", 8)
reviewer2.rate_hw(student2, "Python", 10)
reviewer2.rate_hw(student2, "JavaScript", 9)

student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Git", 8)
student2.rate_lecturer(lecturer2, "Python", 10)
student2.rate_lecturer(lecturer2, "JavaScript", 9)

print("== Проверяющие ==")
print(reviewer1)
print()
print(reviewer2)
print("\n== Лекторы ==")
print(lecturer1)
print()
print(lecturer2)
print("\n== Студенты ==")
print(student1)
print()
print(student2)

print("\nСравнение лекторов:")
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")

print("\nСравнение студентов:")
print(f"{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} == {student2.name}: {student1 == student2}")

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

course_name = "Python"
avg_hw_grade = calculate_avg_hw_grade(students_list, course_name)
avg_lecture_grade = calculate_avg_lecture_grade(lecturers_list, course_name)

print(f"\nСредняя оценка за домашние задания по курсу {course_name}: {avg_hw_grade}")
print(f"Средняя оценка за лекции по курсу {course_name}: {avg_lecture_grade}")

course_name = "Git"
avg_hw_grade = calculate_avg_hw_grade(students_list, course_name)
avg_lecture_grade = calculate_avg_lecture_grade(lecturers_list, course_name)

print(f"\nСредняя оценка за домашние задания по курсу {course_name}: {avg_hw_grade}")
print(f"Средняя оценка за лекции по курсу {course_name}: {avg_lecture_grade}")

course_name = "JavaScript"
avg_hw_grade = calculate_avg_hw_grade(students_list, course_name)
avg_lecture_grade = calculate_avg_lecture_grade(lecturers_list, course_name)

print(f"\nСредняя оценка за домашние задания по курсу {course_name}: {avg_hw_grade}")
print(f"Средняя оценка за лекции по курсу {course_name}: {avg_lecture_grade}")