def find_divisible_numbers(numbers, divisor):
    divisible_numbers = []
    for num in numbers:
        if num % divisor == 0:
            divisible_numbers.append(num)
    return divisible_numbers

numbers = [1, 3, 5]
divisor = 2
divisible_numbers = find_divisible_numbers(numbers, divisor)
print(divisible_numbers)