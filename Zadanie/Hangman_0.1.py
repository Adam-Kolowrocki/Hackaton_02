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
clear = '\n' * 20
round_counter = 12
user_letters = ''
final_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                SORRY YOU'RE DEAD
    ___|___             
'''
initial_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                TRY NOT TO HANG
    ___|___             
'''
fireworks = '''
         .* *.               `o`o`
         *. .*              o`o`o`o      ^,^,^
           * \               `o`o`     ^,^,^,^,^
              \     ***        |       ^,^,^,^,^
               \   *****       |        /^,^,^
                \   ***        |       /
    ~@~*~@~      \   \         |      /
  ~*~@~*~@~*~     \   \        |     /
  ~*~@smd@~*~      \   \       |    /     #$#$#        .`'.;.
  ~*~@~*~@~*~       \   \      |   /     #$#$#$#   00  .`,.',
    ~@~*~@~ \        \   \     |  /      /#$#$#   /|||  `.,'
_____________\________\___\____|_/______/_________|\/\___||______
'''


def comp_choice():
    random_word = choice(words).upper()
    return random_word


def user_type():
    print(clear)
    hidden_word = game_start()
    while round_counter > 0:
        # print(hidden_word)
        print(f'You have {round_counter} tries left to find the word.')
        print(f'Till now You tried letters -- {user_letters} --')
        user_letter = input(f'Type a letter or guess the word -> ')
        user_letter = user_letter.upper()
        if len(user_letter) > 1:
            print(f'.........idę w word_check.....')
            word_check(user_letter)
            return
        else:
            check_previous(user_letter)
    hanged()


def hanged():
    print(final_hangman)
    print(f'You haze used all Your 12 chances with no luck...')


def end_congratulation():
    print(fireworks)
    print(f' Congratulation, You have won the game in {13 - round_counter} round !!!')


def word_check(user_letter):
    control_word = game_start()
    print(f'............jestem w word_check..........')
    print(control_word)
    print(user_letter)
    if user_letter == control_word:
        end_congratulation()
    else:
        round_counter -= 1
        print(f' This is not that word...')
        print(f'Try again...')
        print(f'You have {round_counter} tries left.')
        user_type()


def check_previous(user_letter):
    if user_letters.find(user_letter) > 0:
        print(f"You have already try this letter. Can't do dhis again.")
        print(f'Previously used letters ar: {user_letters}')
        print(f'You still have {round_counter} tries left.')
        user_type()
    else:
        user_letters += user_letter
        hangman_chech(user_letter)


def hangman_check(user_letter):
    hang_word = game_start()
    if hang_word.find(user_letter) == -1:
        not_in_word(user_letter)
    else:
        in_word(user_letter)


def not_in_word(user_letter):
    print(f'Letter "{user_letter}" is not in HANGMAN word...')
    round_counter -= 1
    print(f'You have {round_counter} tries left.')
    print(f'Previously used letters ar: {user_letters}')
    user_type()


def in_word(user_letter):
    hang_word = game_start()
    hidden_word = game_start()
    for i in range(0, len(hang_word)):
        while hang_word.find(user_letter) > -1:
            i = hang_word.find(user_letter)
            hidden_word = hidden_word[: i] + user_letter + hidden_word[i + 1:]
            hang_word = hang_word[: i] + '*' + hang_word[i + 1:]
            print(f'Previously used letters ar: {user_letters}')


def game_start():
    print(clear)
    hang_word = comp_choice()
    control_word = comp_choice()
    print(f'Word for You is {len(hang_word)} letters long.')
    hidden_word = '_' * len(hang_word)
    print(hidden_word)
    print(hang_word)
    print(f'You have 12 chances to win or hang !!!')
    print(initial_hangman)
    input(f'Press ENTER to continue...')
    user_type()
    return hang_word, control_word, hidden_word


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
        game_start()
    else:
        print(clear)
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
