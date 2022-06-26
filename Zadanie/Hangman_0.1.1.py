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
from colorama import Fore
random_words = ['proletariat', 'marm', 'bike', 'motorbike', 'tower', 'microphone', 'elevation', 'drop', 'perturbations']
jobs = ['prestidigitator', 'surgeon', 'anesthesiologist', 'bricklayer', 'roofer', 'mainer', 'metallurgist']
countries = ['libya', 'australia', 'brazil', 'kazakhstan', 'mauritania', 'tanzania', 'turkey', 'thailand']
clear = '\n' * 20

initial_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                TRY NOT TO HANG
    ___|___             
'''
hangman_1 = '''






    ___             
'''
hangman_2 = '''






    ___ ___             
'''
hangman_3 = '''




       |       
       |      
    ___|___             
'''
hangman_4 = '''
       ┌
       |       
       |       
       |       
       |       
       |              
    ___|___             
'''
hangman_5 = '''
       ┌--------
       |        
       |        
       |       
       |       
       |                
    ___|___             
'''
hangman_6 = '''
       ┌--------┐
       |        
       |        
       |       
       |       
       |               
    ___|___             
'''
hangman_7 = '''
       ┌--------┐
       |        |
       |        
       |        
       |       
       |                
    ___|___             
'''
hangman_8 = '''
       ┌--------┐
       |        |
       |        O
       |       
       |       
       |                
    ___|___             
'''
hangman_9 = '''
       ┌--------┐
       |        |
       |        O
       |        ┼
       |       
       |        
    ___|___             
'''
hangman_10 = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       
       |               
    ___|___             
'''
hangman_11 = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴
       |                
    ___|___             
'''
final_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                SORRY YOU'RE DEAD
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


def comp_choice(category):
    if category == 'C':
        random_word = choice(countries).upper()
    elif category == 'J':
        random_word = choice(jobs).upper()
    else:
        random_word = choice(random_words).upper()
    return random_word


def end_congratulation():
    print(clear)
    print(Fore.GREEN + fireworks)
    print(f' Congratulation, You have won the game !!!')
    input(f'Press ENTER to go back to manu...')
    menu()
    return


def end_game_over(control_word):
    print(Fore.RED + final_hangman)
    print(f'You Lost and You have been hanged!!!')
    print(f'The word You were looking for was: "{control_word}".')
    input(f'Press ENTER to continue...')
    menu()
    return


def round_play(hang_word, hidden_word):
    control_word = hang_word
    round_counter = 12
    user_letters = ''
    while round_counter > 0:
        user_letter = input(f'Type a letter or guess the word -> ')
        user_letter = user_letter.upper()

        def hangman():
            if round_counter == 11:
                print(hangman_1)
            elif round_counter == 10:
                print(hangman_2)
            elif round_counter == 9:
                print(hangman_3)
            elif round_counter == 8:
                print(hangman_4)
            elif round_counter == 7:
                print(hangman_5)
            elif round_counter == 6:
                print(hangman_6)
            elif round_counter == 5:
                print(hangman_7)
            elif round_counter == 4:
                print(hangman_8)
            elif round_counter == 3:
                print(hangman_9)
            elif round_counter == 2:
                print(hangman_10)
            elif round_counter == 1:
                print(hangman_11)

        def info_show():
            hangman()
            print('\n')
            print(f'The word looks like this:   {hidden_word}   ')
            print('\n')
            print(f'You have {round_counter} tries left.')
            print('\n')
            print(f'Previously used letters ar: {user_letters}')
            return

        if len(user_letter) > 1:
            if user_letter == control_word:
                end_congratulation()
                break
            else:
                print(clear)
                print(f' "{user_letter}" is not that word. Try again...')
                round_counter -= 1
                info_show()
                continue
        elif len(user_letter) < 1:
            continue
        else:
            if user_letters.find(user_letter) >= 0:
                print(clear)
                print(f"You have already tried this letter. Can't do this again.")
                info_show()
                continue
            else:
                user_letters += user_letter
                if hang_word.find(user_letter) == -1:
                    print(clear)
                    print(f'Letter "{user_letter}" is not in HANGMAN word...')
                    round_counter -= 1
                    info_show()
                    continue
                else:
                    for i in range(0, len(hang_word)):
                        while hang_word.find(user_letter) > -1:
                            i = hang_word.find(user_letter)
                            hidden_word = hidden_word[: i] + user_letter + hidden_word[i + 1:]
                            hang_word = hang_word[: i] + '*' + hang_word[i + 1:]
                            if hidden_word == control_word:
                                end_congratulation()
                                break
                            else:
                                print(clear)
                                print(f'Letter {user_letter} is in the HANGMAN word.')
                                info_show()
                                break
    print(clear)
    end_game_over(control_word)
    return


def game_start(category):
    hang_word = comp_choice(category)
    if category == 'C':
        cat = 'Countries'
    elif category == 'J':
        cat = 'Jobs'
    else:
        cat = 'Random words'
    print(clear)
    print(initial_hangman)
    print('\n' * 3)
    print(f'You have 12 chances to win or hang !!!')
    print(f'Word for You is from category "{cat}" and it is {len(hang_word)} letters long.')
    hidden_word = '_' * len(hang_word)
    print('\n' * 3)
    print(f'And it looks like this:     {hidden_word}')
    print('\n' * 3)
    input(f'Press Enter to continue...')
    return round_play(hang_word, hidden_word)


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

        def categories():
            print(f'You can chose from categories. Type: ')
            print(f'J - for jobs,')
            print(f'C - for countries,')
            print(f'R - for random words.')
            category = input(f'What is Your choice ->')
            category = category.upper()
            correct = ['J', 'C', 'R']
            if category in correct:
                return category
            else:
                print(clear)
                categories()

        game_start(categories())
    else:
        print(clear)
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
