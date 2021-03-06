# Zadanie 00 - książka numerów telefonicznych
# Etap 1:
# Stwórz skrypt w którym:
#     Utworzona zostanie pusta lista lista_numerow.
#     Utworzony zostanie słownik wpis o kluczach imie i numer.
#     Wypełnij go wybranymi przez ciebie wartościami, odpowiednio typu str i int.
#     W osobnej linii do lista_numerow dodany zostanie słownik wpis.
#     Lista lista_numerow zostanie zapisana do pliku ksiazka_numerow.json w formacie JSON.

# Etap 2:
# Wewnątrz skryptu stwórz funkcję, która będzie wczytywać z klawiatury dane do nowego wpisu,
# a następnie doda go do listy wpisów. Funkcja ma:
#  Przyjmować jeden argument: lista, w którym przekazywać będziemy listę, do której funkcja
#  będzie dodawać wpis.
#  Wczyta z klawiatury imię oraz numer.
#  Stworzy słownik analogiczny do tego w etapie 1 i doda go na koniec przekazanej w argumencie listy.
#
# Rozszerzenie:
#  Jeśli Użytkownik nie wpisał poprawnej liczby całkowitej jako numer,
#  program ma poinformować Użytkownika o tym fakcie i nie dodawać niczego do listy,
#  ale nie przerywać pracy całego programu.


import json


def save(numbers_list):
    with open('numbers_book.json', 'w') as plik:
        json.dump(numbers_list, plik)


def dict_import(lista):
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
        return save(numbers_list)
    return


numbers_list = []
entry = {'name': 'Adam', 'number': 601001554}
numbers_list.append(entry)
save(numbers_list)
dict_import(numbers_list)



# Etap 3:
# Stwórz funkcję wczytaj_liste_wpisow, która nie przyjmuje żadnego argumentu.
# Funkcja ta ma wczytać zawartość pliku ksiazka_numerow.json jako Pythonowy obiekt
# (należy użyć funkcji json.load())
#         Funkcja ma ZWRÓCIĆ wczytany obiekt.
#     Zastosuj wyrażenie if __name__ == '__main__' do oddzielenia wykonywanego kodu od definicji funkcji.
#     Przepisz program tak, aby używając zadeklarowanych funkcji program wykonał kolejne działania:
#         wczytał zapisane dane z ksiazka_numerow.json
#         wczytał z klawiatury dane do nowego wpisu.
#         zapisał dane z powrotem do ksiazka_numerow.json lub pod inną nazwą podaną przez użytkownika
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