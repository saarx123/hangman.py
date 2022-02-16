HANGMAN_ASCII_ART = """Welcome to the game Hangman \n
 _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
"""
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, MAX_TRIES)


letter_guessed = input('guess a letter: ').lower()
old_letters_guessed = []


def check_valid_input(letter_guessed, old_letters_guessed):
    """input check from user, it first check if the the string from the user is 1 if not it return false
    second it check that there is no sign in the string if yes return False.
    thirtd it check if the string is in the old_letter_guessed if yes return false.
    forth it check if the string is in the alpabet and not in the old_letter_guessed list and return True"""
    if len(letter_guessed) != 1:
        return False
    elif letter_guessed not in 'abcdefghijklmnopqrstuvwxyz':
        return False
    elif letter_guessed in old_letters_guessed:
        return False
        """if input is one letter and not in old letters list"""
    elif letter_guessed in 'abcdefghijklmnopqrstuvwxyz' and letter_guessed not in old_letters_guessed:
        return True


def not_vaild(old_letters_guessed):
    """"print X and add to list "->" between letters"""
    print("X")
    print(" -> ".join(sorted(old_letters_guessed)))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """function that check if the letter work by the check_vaild_input function.
    and check if the letter show in the old_letter_guessed, if not then add it to the old letter list and return True.
    if the letter show in the old_letter_guessed list then it print the not_vaild function with all the list and return False"""
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        return True
    elif check_valid_input(letter_guessed, old_letters_guessed) == False:
        old_letters_guessed
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    secret_word_list = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_list.append(letter + " ")
        else:
            secret_word_list.append(" _")
    result = ''.join(secret_word_list)
    return result


def check_win(secret_word, old_letters_guessed):
    if ''.join(show_hidden_word(secret_word, old_letters_guessed).split()) in secret_word:
        return True
    else:
        return False
