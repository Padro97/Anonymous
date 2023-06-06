def to_uppercase(input_string):
    output_string = ""
    for char in input_string:
        if "a" <= char <= "z":
            output_string += chr(ord(char) - 32)
        else:
            output_string += char
    return output_string

input_string = input("Введите строку: ")
result = to_uppercase(input_string)
print("Результат: ", result)