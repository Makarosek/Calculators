# Если исходное число больше 10 - делим его на 10
# Если меньше - по степеням переводим в 10-ю
# Потом из 10-й в нужную

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=<>'

startSystem = int(input('Введите исходную систему исчисления от двоичной до пятидесятичной.\n'))

while startSystem not in range(2,51):
    print('Ошибка ввода. Введите целое число от 2х до 50')
    startSystem = int(input())

inputNumber = input('Введите исходное число\n')

lastSystem = int(input('Введите систему, в которую хотите перевести число.\nТак же от двоичной до десятичной.\n'))

while lastSystem not in range(2,51):
    print('Ошибка ввода. Введите целое число от 2х до 50')
    lastSystem = int(input())

def TranslateTo10th(startSystem, inputNumber):
    finishNumber = []
    summ = 0

    print('''Получим число в десятичной системе.
    ''')

    for i in range(len(inputNumber)):
        finishNumber.append(alphabet.find(inputNumber[-i - 1]) * startSystem**i)
        print(alphabet.find(inputNumber[-i - 1]), '*', startSystem, '^', i, '=', finishNumber[i], '.')
    for num in finishNumber:
        summ += num
    print()
    print('Число', inputNumber, 'в десятичной сичтеме будет равно', summ, '.')
    print()
    return summ

print()

NumberIn10th = TranslateTo10th(startSystem, inputNumber) if startSystem != 10 else inputNumber

def TranslateToLast(NumberIn10th, lastSystem):
    result = []

    print('Переведём число из десятичной системы в конечную, деля его на основание системы и записывая остатки.')
    print()

    while NumberIn10th > lastSystem:
        result.append(alphabet[NumberIn10th % lastSystem])

        print(NumberIn10th, 'при делении на', lastSystem, 'даёт остаток', result[-1], '.')

        NumberIn10th = NumberIn10th // lastSystem

    print('Допишем в начале', alphabet[NumberIn10th])

    result.append(alphabet[NumberIn10th])

    print()
    print('Число в конечной системе счисления будет равно', end=' ')
    for k in range(len(result)):
        print( result[-(k + 1)], end = '')
    print('.')

if lastSystem ==10:
    print('Результат -', NumberIn10th)
    exit(0)

TranslateToLast(NumberIn10th, lastSystem)



