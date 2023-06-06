def generate_pseudonym():
    FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Energy', 'F': 'Function', 'G': 'Gloom', 'H': 'Holo', 'I': 'Inovation', 'J': 'Jealous', 'K': 'Katana', 'L': 'Logic', 'M': 'Malware', 'N': 'Negative', 'O': 'Operative', 'P': 'Paragon', 'Q': 'Quant', 'R': 'Recursive', 'S': 'Seismic', 'T': 'Triangle', 'U': 'Ultra', 'V': 'Violent', 'W': 'WiFi', 'X': 'X-ray', 'Y': 'Yell', 'Z': 'Zephyr'}
    SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'E': 'Enormous', 'F': 'Field', 'G': 'Garbage', 'H': 'Half-life', 'I': 'Intranet', 'J': 'Jack', 'K': 'Killer', 'L': 'Lava', 'M': 'Madness', 'N': 'Nickname', 'O': 'Ops', 'P': 'Payload', 'Q': 'Qubit', 'R': 'Radiant', 'S': 'Sygnus', 'T': 'T-Rex', 'U': 'Unity', 'V': 'Vox','W': 'Worm','X': 'Xeon','Y': 'Yawn','Z': 'Zeppelin'}
    first_name = input("Введите ваше имя: ").capitalize()
    surname = input("Введите вашу фамилию: ").capitalize()
    print("Ваше имя и фамилия: " + first_name + " " + surname)
    if not first_name.isalpha() or not first_name[0].isupper():
        print("Ваше имя должно начинаться с буквы от A до Z.")
    if not surname.isalpha() or not surname[0].isupper():
        print("Ваша фамилия должна начинаться с буквы от A до Z.")
    else:
        pseudonym = FIRST_NAME[first_name[0].upper()] + " " + SURNAME[surname[0].upper()]
        print("Ваш псевдоним: " + pseudonym)

generate_pseudonym()