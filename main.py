class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__grades = []  

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)

    def remove_grade(self, grade):
        if grade in self.__grades:
            self.__grades.remove(grade)

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def show_info(self):
        return f"{self.name} {self.surname}, yosh: {self.age}, o'rtacha baho: {self.get_average():.2f}"
