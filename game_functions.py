import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    def pick_value(poss_values):
        return poss_values[len(poss_values) // 2]


# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    pass

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    flag = True
    for i in range(len(word)):
        if word[i] == letter:
            flag = False
            board[i] = letter
    if flag is True:
        return False
    return True
