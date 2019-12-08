from colorama import Fore, Back, Style
import colorama


def answer(text, case):
    if case == "NO":
        print(Fore.RED + text)
    elif case == "YES":
        print(Fore.GREEN + text)
    elif case == "NEUTRAL":
        print(Fore.BLACK + text)
    else:
        print("error")


Questions = [
    'Какое (какие) из этих устройств является устройством вывода?',
    'Какое (какие) из этих устройств является устройством ввода?',
    ' 15 человек смотрели фильм «Обитаемый остров», \n 11 человек – фильм «Стиляги», из них 6 смотрели и \n «Обитаемый остров», и «Стиляги».\nСколько человек смотрели только фильм «Стиляги»?',
    'Переведите десятичное число 728 в двоичную систему записи. Что получилось?',
    'Переведите двоичное число 1011011 в десятичную систему записи. Что получилось?',
    'Какие из ниже приведённых утверждений о десятипальцевом методе печати являются верными? В ответе укажите номера верных утверждений через запятую.'
]

Variants = [
    ' Манипулятор мышь\n Монитор\n Клавиатура\n Микрофон',
    ' Клавиатура\n Принтер\n Монитор\n Манипулятор мышь',
    ' ', ' ', ' ',
    ' 1. При десятипальцевом методе печати буква "Э" нажимается мизинцем правой руки.\n 2. При десятипальцевом методе печати пробел нажимается средним пальцем.\n 3. При десятипальцевом методе печати пробел можно нажимать большим пальцем любой руки.\n 4. Десятипальцевый метод был разработан для глухих людей'
]

Right_answers = [  # Правильные ответы
    ['МОНИТОР'],
    ['КЛАВИАТУРА', 'МАНИПУЛЯТОР МЫШЬ'],
    ['5'],
    ['1011011000'],
    ['91'],
    ['1', '3']
]

answerCounter = 6
Grade = 0
YourAnswers = []
YourGrades = []
colorama.init(autoreset = True)
student = input("Укажите ваш логин (идентификатор):")

for i in range(answerCounter):
    print(colorama.ansi.clear_screen())
    print(Style.RESET_ALL)
    print(f"Задание № {i+1}")
    answer(Questions[i], 'NEUTRAL')
    answer(Variants[i], 'NEUTRAL')
    Your_answer = input("Ваш ответ: ").upper().split(", ")
    YourAnswers.append(Your_answer)
    set_to_be = set(Right_answers[i])
    set_is = set(Your_answer)
    good_set = set_to_be.intersection(set_is)
    extra_set = set_is-set_to_be
    Grade = max(len(good_set)-len(extra_set),0)/len(set_to_be)
    YourGrades.append(Grade)
    if Grade > 0.99:
        answer('Ваш ответ верный.', 'YES')
    elif Grade == 0.0:
        answer('Ваш ответ неверный.', 'NO')
    else:
        answer('Ваш ответ неполный.', 'NO')
    # print(good_set, extra_set)

Grade = sum(YourGrades) / answerCounter * 5

if Grade >= 4:
    answer(f"Молодец! У вас замечательная оценка! Ваша оценка {Grade:.0f} из 5.", 'YES')
else:
    answer(f"Вы пока что не молодец. Старайтесь лучше. Ваша оценка {Grade:.0f} из 5.", 'NO')


print()
colorama.deinit()
colorama.init(autoreset = False)
print(Back.LIGHTYELLOW_EX + 'Протокол контрольного тестирования.')
print('Имя студента: ' + student)
print(f'Оценка за тест: {Grade:.0f} из 5.')

for i in range(answerCounter):
    print(Back.LIGHTYELLOW_EX + Questions[i])
    print(Variants[i])
    if YourGrades[i] > 0.99:
        case = 'YES'
    else:
        case = 'NO'
    answer(f"Ответ {YourAnswers[i]} оценён на {YourGrades[i]:1.2f} баллов.", case)
    # print(Style.RESET_ALL, f"Правильный ответ: {Right_answers[i]}")
    print(f"Правильный ответ: {Right_answers[i]}")
    print(Style.RESET_ALL + Back.LIGHTYELLOW_EX)
