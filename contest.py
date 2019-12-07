from colorama import Fore
import colorama


def answer (text, case):
    if case == "NO":
        print(Fore.RED + text)
    elif case == "YES":
        print(Fore.GREEN + text)
    elif case == "NEUTRAL":
        print(Fore.BLACK + text)
    if not(case in ['YES', 'NO', 'NEUTRAL']):
        print("error")


Questions = [
    '1. \n Какое (какие) из этих устройств является устройством вывода?',
    '2. \n Какое (какие) из этих устройств является устройством ввода?',
    '3. \n 15 человек смотрели фильм «Обитаемый остров», \n 11 человек – фильм «Стиляги», из них 6 смотрели и \n «Обитаемый остров», и «Стиляги».\nСколько человек смотрели только фильм «Стиляги»?',
    '4. \n Переведите десятичное число 728 в двоичную систему. Что получилось?',
    '5. \n Переведите двоичное число 1011011 в десятичную систему. Что получилось?',
    '6. \n Какие из ниже приведённых утверждений о десятипальцевом методе печати являются верными? (в ответе укажите номера верных утверждений через запятую)'
]

Variants = [
    ' Мышь компьютерная \n Монитор \n Клавиатура \n Микрофон',
    ' Клавиатура \n Принтер \n Монитор \n Мышь компьютерная',
    ' ', ' ', ' ',
    '1. При десятипальцевом методе печати буква "Э" нажимается мизинцем правой руки. \n 2. При десятипальцевом методе печати пробел нажимается средним пальцем. \n 3. При десятипальцевом методе печати пробел можно нажимать большим пальцем любой руки. \n 4. Десятипальцевый метод был разработан для глухих людей'
]


Right_answers = [
    'Монитор',
    'Клавиатура, мышь компьютерная',
    '5',
    '1011011000',
    '91',
    '1, 3'
] # Правильные ответы не подсматривать!!

answerCounter = 6
Grade = 0
YourAnswers = []
colorama.init()

for i in range(1, answerCounter + 1):
    # print(colorama.ansi.clear_screen())
    answer(Questions[i-1], 'NEUTRAL')
    answer(Variants[i-1], 'NEUTRAL')
    Your_answer = input("Ваш ответ: ")
    YourAnswers.insert(i, Your_answer)
    Right_answer = Right_answers[i - 1]
    if Your_answer == Right_answer:
        answer('Ваш ответ верный.', 'YES')
        Grade += 1
    else:
        answer('Ваш ответ неверный.', 'NO')

Grade = Grade/answerCounter * 5

if Grade >= 4:
    answer("Молодец! У вас замечательная оценка! Ваша оценка " + str(int(Grade)) + " из 5.", 'YES')
else:
    answer("Вы пока что не молодец. Старайтесь лучше. Ваша оценка " + str(int(Grade)) + " из 5.", 'NO')

answer('', 'NEUTRAL')
print('Ответы: ')

for i in range (answerCounter):
    answer(Questions[i], 'NEUTRAL')
    answer(Variants[i], 'NEUTRAL')
    Your_answer = YourAnswers[i]
    Right_answer = Right_answers[i]
    if Your_answer == Right_answer:
        answer('Ваш ответ: ' + Your_answer, 'YES')
    else:
        answer('Ваш ответ: ' + Your_answer, 'NO')
    answer('', 'NEUTRAL')
    print("Правильный ответ: " + Right_answer)
















































































