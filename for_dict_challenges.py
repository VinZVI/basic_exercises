print('<<<<<<< Задание 1 >>>>>>>')
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

count_names = {}
for student in students:
    name = student['first_name']
    value = count_names.setdefault(name, 0)
    value += 1
    count_names[name] = value

for name, value in count_names.items():
    print(f'{name}: {value}')


print('\n<<<<<<< Задание 2 >>>>>>>')
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
count_names = {}
for student in students:
    name = student['first_name']
    value = count_names.setdefault(name, 0)
    value += 1
    count_names[name] = value
max_name = max(count_names, key=count_names.get)
print(f'Самое частое имя среди учеников: {max_name}')


print('\n<<<<<<< Задание 3 >>>>>>>')
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for number, class_students in enumerate(school_students, start=1):
    count_names = {}
    for student in class_students:
        name = student['first_name']
        value = count_names.setdefault(name, 0)
        value += 1
        count_names[name] = value
    max_name = max(count_names, key=count_names.get)
    print(f'Самое частое имя в классе {number}: {max_name}')


print('\n<<<<<<< Задание 4 >>>>>>>')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_student in school:
    count_boys = 0
    count_girls = 0
    for students in class_student['students']:
        if is_male.get(students['first_name']):
            count_boys += 1
        else:
            count_girls += 1
    print(f'Класс {class_student["class"]}: девочки {count_girls}, мальчики {count_boys}')



print('\n<<<<<<< Задание 5 >>>>>>>')
# По информации об учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
class_count = {}
for class_student in school:
    count_boys = 0
    count_girls = 0
    for students in class_student['students']:
        if is_male.get(students['first_name']):
            count_boys += 1
        else:
            count_girls += 1
    class_count.setdefault(class_student['class'], [count_boys, count_girls])
def func(x):
    return class_count.get(x)[0]

max_boys = max(class_count, key=func)
max_girls = max(class_count, key=lambda x: class_count.get(x)[1])
print(f'Больше всего мальчиков в классе {max_boys}')
print(f'Больше всего девочек в классе {max_girls}')

