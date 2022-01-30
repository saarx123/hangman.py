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
    """input check from user"""
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
    print("X")
    print(" -> ".join(sorted(old_letters_guessed)))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        print(old_letters_guessed)
        return True
    elif check_valid_input(letter_guessed, old_letters_guessed) == False:
        not_vaild(old_letters_guessed)
        return False


def main():
    print(try_update_letter_guessed(letter_guessed, old_letters_guessed))


if __name__ == '__main__':
    main()
