# Zadanie 03 - wisielec
# Etap 1:
#  Gracz powinien mieć listę wykorzystanych liter na widoku
#  i jeśli dana litera jest wykorzystana, nie powinien móc jej użyć ponownie.
# Etap 2:
#  Niech pojawi się tytułowy wisielec (hints).
# Etap 3:
#  Jeśli użytkownik przegra, pokoloruj wisielca na czerwono za pomocą modułu, np. import color.
# Rozszerzenie
# Wykorzystaj moduł turtle, by narysować wisielca.

from random import choice
words = ['proletariat', 'marmur', 'koszykówka', 'podwieczorek', 'mormyszka', 'prestidigitator', 'przewyższenie', 'deniwelacja', 'perturbacje', 'parkingowy', 'Konstantynopol', 'czomolungma']
clear = '\n' * 40


def comp_choice():
    random_word = choice(words).upper()
    return random_word


final_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                SORRY YOU'RE DEAD
    ___|___             
'''


def round_play():
    hang_word, hidden_word = game_start()
    print(hidden_word)         # do wykasowania
    print(hang_word)            # do wykasowania
    round_counter = 12
    user_letters = ''
    print(user_letters)         # do wykasowania
    while round_counter > 0:
        user_letter = input(f'Type a letter -> ')
        user_letter = user_letter.upper()
        if user_letters.find(user_letter) > 0:
            print(f"You have already try this letter. Can't do dhis again.")
            print(f'Previously used letters ar: {user_letters}')
            continue
        else:
            user_letters += user_letter
            print(user_letters)     # do wykasowania

        if hang_word.find(user_letter) == -1:
            print(f'Letter "{user_letter}" is not in HANGMAN word...')
            print(f'Previously used letters ar: {user_letters}')
            round_counter -= 1
            print(f'You have {round_counter} tries left.')
            continue
        else:
            for i in range(0, len(hang_word)):
                while hang_word.find(user_letter) > 0:
                    print(f'wynik find = {hang_word.find(user_letter)}')
                    i = hang_word.find(user_letter)
                    hidden_word = hidden_word[0: i] + user_letter + hidden_word[i + 1 :]
                    print(hidden_word)
                    hang_word = hang_word[0: i] + '_' + hang_word[i + 1 :]
                    print(hang_word)
                    print(f'Previously used letters ar: {user_letters}')
        print(hidden_word)


def game_start():
    print(clear)
    hang_word = comp_choice()
    print(f'Word for You is {len(hang_word)} letters long.')
    hidden_word = '_' * len(hang_word)
    print(hidden_word)
    print(f'You have 12 chances to win !!!')
    return hang_word, hidden_word


def menu():
    print(clear)
    print(f'Wellcome HANGMAN')
    print(f'Do You want to hang ??')
    user_choice = input(f'Y/N ->')
    if user_choice.lower() == 'n':
        print(f'If You say so....')
        print(f'Bye Bye.')
        return
    elif user_choice.lower() == 'y':
        round_play()
    else:
        print(clear)
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
