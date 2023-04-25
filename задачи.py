# №1
# задаем исходные данные
numbers = [1, 2, 3, 4, 5, 6]
divisor = 2
# создаем пустой массив, в который будем добавлять числа, которые делятся на делитель
divisible_numbers = []
# перебираем все числа в исходном массиве
for num in numbers:
    # если число делится на делитель, добавляем его в массив
    if num % divisor == 0:
        divisible_numbers.append(num)
# выводим на консоль массив чисел, которые делятся на делитель
print(divisible_numbers)


# №2
numbers = [0, 1, 2, 3, 4, 5, 6]
divisor = 4
divisible_numbers = []
for num in numbers:
    if num % divisor == 0:
        divisible_numbers.append(num)
print(divisible_numbers)

# №3
numbers = [0, 1, 2, 3, 4, 5, 6]
divisor = 4
divisible_numbers = []
for num in numbers:
    if num % divisor == 0:
        divisible_numbers.append(num)
print(divisible_numbers)

# №4
numbers = [0]
divisor = 4
divisible_numbers = []
for num in numbers:
    if num % divisor == 0:
        divisible_numbers.append(num)
print(divisible_numbers)

# №5
numbers = [1, 3, 5]
divisor = 2
divisible_numbers = []
for num in numbers:
    if num % divisor == 0:
        divisible_numbers.append(num)
print(divisible_numbers)


# Да, оптимальное решение!
# Следующей задачей будет преобразовать данный код (один из предложенных примеров) в функцию.
# Тогда мы сократим решение и запишем его и сможем использовать один код много раз

# Не забудь добавить ее через гит на локальном устройстве
