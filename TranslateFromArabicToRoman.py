#1 = I
#5 = V
#10 = X
#50 = L
#100 = C
#500 = D
#1000 = M
#5000 = W

arabicNumbers = '0123456789'
arabicNumver = input('Введите целое число от 1 до 8999\n')

romanNumbers = ['IV', 'XL', 'CD', 'MW']

result = []

for i in range(len(arabicNumver)):
    if 0 < int(arabicNumver[-1]) < 4:
        result.append(romanNumbers[i][0] * int(arabicNumver[-1]))
        print("Цифра", int(arabicNumver[-1]) * 10**i, 'в римской системе записывается как', result[i])

    elif int(int(arabicNumver[-1]) == 4):
        result.append(romanNumbers[i])
        print("Цифра", int(arabicNumver[-1]) * 10**i, 'в римской системе записывается как', result[i])

    elif 4 < int(arabicNumver[-1]) < 9:
        result.append(romanNumbers[i][1] + (int(arabicNumver[-1]) - 5) * romanNumbers[i][0])
        print("Цифра", int(arabicNumver[-1]) * 10**i, 'в римской системе записывается как', result[i])

    elif int(arabicNumver[-1]) == 9:
        result.append(romanNumbers[i][0] + romanNumbers[i + 1][0])
        print("Цифра", int(arabicNumver[-1]) * 10**i, 'в римской системе записывается как', result[i])

    arabicList = list(arabicNumver)
    arabicList[-1] = ""
    arabicNumver = "".join(arabicList)

print('Полная запись - ', end = ' ')
for i in range(len(result)):
    print(result[-(i+1)], end=' ')