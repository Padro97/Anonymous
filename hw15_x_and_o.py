def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
s = input("Введите строку: ")
if xo(s):
    print("True")
else:
    print("False")
    
# Так, ну вот через функцию решать пока это рано) 
# Давай мы это решение напишем также, но без функции.
# Его также надо внести через git с локального устройства
