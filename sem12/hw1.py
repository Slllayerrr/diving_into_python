# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. (isalpa and istitle)
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv

class Text:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __set_name__(self, owner, name):
        self.param1_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param1_name)

    def __set__(self, instance, value):
        if self.param1(value) and self.param2(value):
            setattr(instance, self.param1_name, value)
        else:
            raise ValueError(f'{value} - плохое имя!')


class Student:
    name = Text(str.istitle, str.isalpha)

    def __init__(self, name, subject_file):
        self.name = name
        self.subject_file = subject_file
        self.subjects = {str(self.name): {}}
        self.grades = {str(grd): [] for grd in self.load_subject()}
        self.test_scores = {str(test): [] for test in self.load_subject()}
        self.avg_test = 0
        self.avg_grade = 0

    def load_subject(self):
        uniq_sub = set()
        with open(f'{self.subject_file}', 'r', newline='', encoding='utf-8') as csv_f:
            csv_read = csv.reader(csv_f, dialect='excel-tab')
            for elem in csv_read:
                uniq_sub.update(elem)
        return uniq_sub

    def add_grade(self, subject, grade):
        if int(grade) < 2 or int(grade) > 5:
            raise ValueError('Оценка должна быть от 2 до 5!')
        lst_grade = grade
        for key, value in self.grades.items():
            if key == subject:
                if value is not None:
                    value.append(lst_grade)
                self.grades[subject] = value
                lst_grade = value
            for _ in self.load_subject():
                self.subjects[str(self.name)][subject] = {'Оценки': lst_grade, 'Тест': self.test_scores[subject]}
        return self.grades

    def add_test_score(self, subject, test_score):
        if int(test_score) < 0 or int(test_score) > 100:
            raise ValueError('Оценка должна быть от 0 до 100!')
        lst_test = test_score
        for key, value in self.test_scores.items():
            if key == subject:
                if value is not None:
                    value.append(lst_test)
                self.test_scores[subject] = value
                lst_test = value
            for _ in self.load_subject():
                self.subjects[str(self.name)][subject] = {'Оценки': self.grades[subject], 'Тест': lst_test}
        return self.test_scores

    def get_avg_test_score(self, subject):
        summ = 0
        for key, value in self.test_scores.items():
            if key == subject:
                for elem in value:
                    summ += elem
                self.avg_test = summ / len(value)
        return self.avg_test

    def get_avg_grade(self):
        summ = 0
        sum_len = 0
        for value in self.grades.values():
            for elem in value:
                summ += elem
            sum_len += len(value)
            self.avg_grade = summ / sum_len
        return self.avg_grade

    def __str__(self):
        return f'Имя студента: {self.name} \nПредметы: {self.load_subject()} \nОценки: {self.grades=} \nСредний балл оценок по всем предметам: {self.avg_grade} \nСредний балл тестов по предмету: {self.avg_test}'


if __name__ == '__main__':
    sub = ['Математика', 'Русский', 'История']
    with open('subject_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel-tab')
        csv_write.writerow(sub)

    student2 = Student('Адам', 'subject_file.csv')
    student2.add_grade('История', 4)
    student2.add_grade('История', 5)
    student2.add_grade('История', 4)
    student2.add_grade('Математика', 4)
    student2.add_grade('Математика', 5)
    student2.add_grade('Русский', 3)
    student2.add_grade('Русский', 4)
    student2.add_test_score('История', 100)
    student2.add_test_score('История', 90)
    student2.add_test_score('Русский', 80)
    student2.add_test_score('Русский', 95)
    student2.add_test_score('Математика', 70)
    student2.add_test_score('Математика', 65)
    student2.subjects
    student2.get_avg_test_score('История')
    student2.get_avg_grade()
    print(student2)
