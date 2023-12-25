#2
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

# вычисляем сумму, произведение и среднее арифметическое
summ = num1 / num2 / num3
prod = num1 * num2 * num3
avg = summ / 3

# выводим результаты
print("delenye:", summ)
print("Произведение чисел:", prod)
print("Среднее арифметическое чисел:", avg)
#3
meters = float(input("tell metrs:"))
print(f"miles: {meters * 1609.34 }")
print(f"dumes: { meters * 39.3701}")
print(f"yards: { meters * 1.09361}")
#1
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
calculate = input(
    'Список операций калькулятора: "+" - сложение \n  "*" - умножение\n '
    'Введите нужную вам операцию: ')
if calculate == '+':
    print(f'Результат вычисления: {a + b}')
elif calculate == '*':
    print(f'Результат вычисления: {a * b}')
