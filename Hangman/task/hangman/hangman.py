# Write your code here

import random

word_list = ["python", "java", "swift", "javascript"]
random.shuffle(word_list)
full_word = word_list[0]
new_word = []
word = []
num_attempts = 8
num_wins = 0
num_lost = 0
format_ok = False
user_input = ""
guess_list = []


def print_menu():
    num_attempts = 8
    global user_input
    print(f"""H A N G M A N # {num_attempts} attempts""")
    text = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
    print(text)
    user_input = input()
    while user_input != "play" and user_input != "results" and user_input != "exit":
        print(text)
        user_input = input()


def check_letter():
    global guess
    global format_ok
    global guess_list
    format_ok = True
    if guess in guess_list:
        print("guess:", guess)
        print("guest_list", guess_list)
        print("You've already guessed this letter.")
        format_ok = False
    elif len(guess) != 1 or guess is False:
        print("Please, input a single letter.")
        format_ok = False
    elif guess.isupper() or not guess.isalpha():
        print("Please, enter a lowercase letter from the English alphabet.")
        format_ok = False
    else:
        guess_list.append(guess)
    return format_ok


def start_game():
    global format_ok
    global guess
    global num_wins
    global num_lost
    global guess_list
    guess_list = []
    num_attempts = 8
    word_list = ["python", "java", "swift", "javascript"]
    random.shuffle(word_list)
    full_word = word_list[0]
    new_word = []
    word = ""
    for i in range(len(full_word)):
        new_word.append("-")
    while "-" in new_word and num_attempts > 0:
        format_ok = False
        print()
        print("".join(new_word))
        print("Input a letter: ")
        guess = input()
        format_isOk = check_letter()
        while not format_isOk:
            print("".join(new_word))
            print("Input a letter: ")
            guess = input()
            format_isOk = check_letter()
        if guess in full_word:
            if guess not in new_word:
                # print(f"# {num_attempts} attempts")
                for i in range(len(full_word)):
                    if guess == full_word[i]:
                        new_word[i] = full_word[i]
            else:
                num_attempts -= 1
                print("No improvements.")
        else:
            num_attempts -= 1
            print(f"That letter doesn't appear in the word.  # {num_attempts} attempts")
        if num_attempts > 0:
            word = "".join(new_word)
    if "-" in word:
        print("You lost!")
        num_lost += 1
    else:
        print(f"You guessed the word {full_word}!")
        print("You survived!")
        num_wins += 1


def print_result():
    global num_wins
    global num_lost
    print(f"You won: {num_wins} times")
    print(f"You lost: {num_lost} times")


while user_input != "exit":
    print_menu()
    if user_input == "play":
        start_game()
    elif user_input == "results":
        print_result()
    else:
        pass
