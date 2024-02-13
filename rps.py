# rps_match uses 2 parameters. 
# - user_choice = You
# - computer_choice = Computer

# The choices are represented like this: 
# 0 = Rock 
# 1 = Paper 
# 2 = Scissors

# This function will compare the user's choice with the computer's choice
# and return a result (see README for instructions) 
    
def rps_match(user_choice, bot_choice):
    # Add your code here
    
    # There are only 3 index in the list, becuase user have three choice which is ROCK, PAPER, and SCISSORS
    index_choice_available = [0,1,2]

    # So, in case user's inpur, or bot's input, not in the list, function will return the Invalid Input
    # It still make sense if we don't check for bot's input, since the Randint function in the main.py, the code will only random from 0 to 2 which is the number in List
    if user_choice not in index_choice_available or bot_choice not in index_choice_available:
        return 'invalid input'
    
    # These code below will check the condition to see if someone win the round or tie
    # If user win, the function will return 1
    # If bot win, then the function will retun -1
    # It tie, function will return 0
    else: 
        if user_choice == 0 and bot_choice == 2:
            return 1
        elif user_choice == 1 and bot_choice == 0:
            return 1
        elif user_choice == 2 and bot_choice == 1:
            return 1
        elif user_choice == 0 and bot_choice == 1:
            return -1
        elif user_choice == 1 and bot_choice == 2:
            return -1
        elif user_choice == 2 and bot_choice == 0:
            return -1
        elif user_choice == 0 and bot_choice == 0:
            return 0
        elif user_choice == 1 and bot_choice == 1:
            return 0
        elif user_choice == 2 and bot_choice == 2:
            return 0
    pass