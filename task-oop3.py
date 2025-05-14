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
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
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


student1 = Student("Иван", "Иванов", "мужской")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]
student1.grades = {"Python": [9, 10, 8], "Git": [8, 9]}

student2 = Student("Мария", "Петрова", "женский")
student2.courses_in_progress = ["Python"]
student2.grades = {"Python": [10, 9, 10]}

lecturer1 = Lecturer("Алексей", "Смирнов")
lecturer1.grades = {"Python": [9, 10, 8]}

lecturer2 = Lecturer("Ольга", "Кузнецова")
lecturer2.grades = {"Python": [10, 9, 10]}

reviewer = Reviewer("Дмитрий", "Васильев")

print("== Проверяющий ==")
print(reviewer)
print("\n== Лектор 1 ==")
print(lecturer1)
print("\n== Лектор 2 ==")
print(lecturer2)
print("\n== Студент 1 ==")
print(student1)
print("\n== Студент 2 ==")
print(student2)

print("\nСравнение лекторов:")
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")

print("\nСравнение студентов:")
print(f"{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} == {student2.name}: {student1 == student2}")