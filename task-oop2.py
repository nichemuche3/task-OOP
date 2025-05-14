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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  


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
            return "Ошибка: Невозможно оценить ДЗ"
        

student1 = Student("Иван", "Сильный", "мужской")
student1.courses_in_progress.append("Python")

student2 = Student("Мария", "Иванова", "женский")
student2.courses_in_progress.append("Python")


lecturer1 = Lecturer("Алексей", "Смирнов")
lecturer1.courses_attached.append("Python")

lecturer2 = Lecturer("Ольга", "Кузнецова")
lecturer2.courses_attached.append("Python")


reviewer1 = Reviewer("Дмитрий", "Васильев")
reviewer1.courses_attached.append("Python")

reviewer2 = Reviewer("Елена", "Соколова")
reviewer2.courses_attached.append("Python")


reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student2, "Python", 8)


student1.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer2, "Python", 8)


print("Оценки студентов:")
print(f"{student1.name}: {student1.grades}")
print(f"{student2.name}: {student2.grades}")

print("\nОценки лекторов:")
print(f"{lecturer1.name}: {lecturer1.grades}")
print(f"{lecturer2.name}: {lecturer2.grades}")