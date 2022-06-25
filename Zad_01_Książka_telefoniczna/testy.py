# test = {x: x ** 2 for x in range(10)}
# print(test)

# entry = {'name': 'Adam', 'number': 601001554,
#          'name': 'Basia', 'number': 609445668,
#          'name': 'Michał', 'number': 508455745,
#          'name': 'Kasia', 'number': 659984475
#         }
# entry = {'name': 'Adam', 'Basia', 'Michał', 'Kasia', 'number': 601001554, 609445668, 508455745, 659984475}
import json


def dict_main():
    numbers_list = []
    entry = {'name': 'Adam', 'number': 601001554}
    numbers_list.append(entry)

    with open('numbers_book.json', 'w') as plik:
        json.dump(numbers_list, plik)
    return


def dict_import(lista):
    print(f'You can add Your own inputs to "numbers_book".')
    user_decision = input(f'Do You want to add ? T/N -> ')
    user_decision.upper()
    if user_decision == 'T':
        user_input_name = input(f'Please, give a name to add -> ')
        user_input_number = input(f'Please, give a number for {user_input_name} -> ')
        user_entry = {user_input_name: user_input_number}
        lista.append(user_entry)
        return lista
    else:
        return


def main():
    dict_main()


if __name__ == "__main__":
    main()