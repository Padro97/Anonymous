def convert_to_uppercase(input_string):
result = ""
for char in input_string:
if 'a' <= char <= 'z':
result += chr(ord(char) - 32)
else:
result += char
return result