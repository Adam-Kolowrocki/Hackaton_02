import json

# numbers_list = []


def save(numbers_list):
    filename = input(f'Podaj nazwę kliku do zapiania książki, bez rozszerzenia -> ')
    with open(f'{filename}.json', 'w') as plik:
        json.dump(numbers_list, plik)


def read_entry_list():
    with open('numbers_book.json') as plik:
        numbers_list = json.load(plik)
    return numbers_list


def dict_import(lista):
    lista = read_entry_list()
    print(f'You can add Your own inputs to "numbers_book".')
    user_decision = input(f'Do You want to add ? T/N -> ')
    user_decision = user_decision.upper()
    while user_decision == 'T':
        user_input_name = input(f'Please, give a name to add -> ')
        try:
            user_input_number = int(input(f'Please, give a number for {user_input_name} -> '))
            user_entry = {user_input_name: user_input_number}
        except ValueError:
            print(f'Wrong number type. Please try again.')
            continue

        lista.append(user_entry)
        return save(lista)
    return


def main():
    read_entry_list()
    dict_import(read_entry_list())


if __name__ == "__main__":
    main()


# Przepisz program tak, aby używając zadeklarowanych funkcji program wykonał kolejne działania:
#   wczytał zapisane dane z ksiazka_numerow.json
#   wczytał z klawiatury dane do nowego wpisu.
#   zapisał dane z powrotem do ksiazka_numerow.json lub pod inną nazwą podaną przez użytkownika
#
# Rozszerzenie 1:
#
# Zmodyfikuj funkcję wczytaj_listę_wpisów tak, aby wypisywała komunikat o liczbie wczytanych wpisów.
# Rozszerzenie 2:
#
# Zmodyfikuj funkcję wczytaj_listę_wpisów tak, aby w przypadku braku pliku ksiazka_numerow.json zwracała pustą listę.
# Rozszerzenie 3:
#
# Zmodyfikuj program tak, aby przed wczytaniem nowego wpisu zapytał się Użytkownika, czy wczytać nowy wpis.
#
#     Jeśli Użytkownik wpisze 't' to rozpocznie się wczytywanie nowego wpisu, a następnie pytanie zostanie ponowione.
#     Jeśli Użytkownik wpisze 'n' to wczytywanie nie rozpocznie się i program będzie kontynuował swoje działanie.
#     Jeśli Użytkownik wpisze cokolwiek innego, pytanie zostanie ponowione.