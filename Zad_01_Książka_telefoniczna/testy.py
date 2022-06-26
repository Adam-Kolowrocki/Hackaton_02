from colorama import Fore
base_string = 'trestidigitator'
print(base_string)
hidden_string = '_______________'
print(hidden_string)
user_letter = 't'


for i in range(0, len(base_string)):
    while base_string.find(user_letter) > -1:
        print(f'wynik find = {base_string.find(user_letter)}')
        i = base_string.find(user_letter)
        print(f'i wynosi {i}')
        hidden_string = hidden_string[: i] + user_letter + hidden_string[i + 1:]
        print(hidden_string)
        base_string = base_string[: i] + '*' + base_string[i + 1:]
        print(base_string)


print(Fore.RED + 'Testowy Text')
