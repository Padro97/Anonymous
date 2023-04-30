s = input('Введите строку: ')
s = s.lower()
cntx = 0
cnto = 0
for i in s:
    if i == 'x':
        cntx += 1
    elif i == 'o':
        cnto += 1
if cntx == cnto:
    print('True')
else:
    print('False')