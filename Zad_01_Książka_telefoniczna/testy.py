base_string = 'prestidigitator'
print(base_string)
hidden_string = '_______________'
print(hidden_string)
user_letter = 't'

while base_string.find(user_letter) > 0:
    print(f'wynik find = {base_string.find(user_letter)}')
    for i in enumerate(base_string):
        i = base_string.find(user_letter)
        print(f'i wynosi {i}')
        hidden_string = hidden_string[0: i - 1] + user_letter + hidden_string[i + 1]
        print(hidden_string)
        base_string = base_string.replace(user_letter, '0')
        print(base_string)
