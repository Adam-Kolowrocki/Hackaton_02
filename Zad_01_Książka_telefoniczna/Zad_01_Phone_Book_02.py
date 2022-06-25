import json


def save(numbers_list):
    filename = input(f'Podaj nazwę kliku do zapiania książki, bez rozszerzenia -> ')
    if filename == '':
        with open(f'numbers_book.json', 'w') as plik:
            json.dump(numbers_list, plik)
    else:
        with open(f'{filename}.json', 'w') as plik:
            json.dump(numbers_list, plik)


def read_entry_list():
    from os.path import exists
    file_exists = exists('/home/adam/Dokumenty/Python-Kurs/Hackaton_02/Zad_01_Książka_telefoniczna/numbers_book.json')
    if file_exists:
        with open('numbers_book.json') as plik:
            numbers_list = json.load(plik)
            print(f'There was {len(numbers_list)} records in file.')
    else:
        print(f'No such a file/directory "numbers_book.json.')
        numbers_list = []
    return numbers_list


def dict_import(lista):
    lista = read_entry_list()
    print(f'You can add Your own inputs to "numbers_book".')
    while True:
        user_decision = input(f'Do You want to add ? T/N -> ')
        user_decision = user_decision.upper()
        if user_decision == 'T':
            user_input_name = input(f'Please, give a name to add -> ')
            while True:
                try:
                    user_input_number = int(input(f'Please, give a number for {user_input_name} -> '))
                    break
                except ValueError:
                    print(f'Wrong number type. Please try again.')
            user_entry = {user_input_name: user_input_number}
            lista.append(user_entry)
            continue
        elif user_decision == 'N':
            return save(lista)
        else:
            print(f'You can chose "T" or "N"')
            continue


def main():
    lista = []
    dict_import(lista)


if __name__ == "__main__":
    main()
