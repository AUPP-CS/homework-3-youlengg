from rps import rps_match
from random import randint

rock = '''
⠀⠀⠀⠀⠀⢄⡶⠷⠒⠒⠺⠿⣶⡠⣀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣪⠏⠀⢀⡤⠂⠀⠀⠀⠈⠛⢽⡤⢴⡄⡀⠀
⣰⡾⠛⠉⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠙⣞⡀
⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠛⠀⢿⠀⢹⣧
⣸⣿⠶⠤⠤⠀⠀⠀⠀⠀⠀⢠⠤⠴⠖⠚⡃⢸⡇⢸⡏
⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠶⠛⠁⣸⣃⣼⠏
⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡻⠋⠁⠀
⠀⠙⢿⣏⠉⠉⠁⠀⠀⠀⠀⠀⠀⣠⣴⡻⠊⠀⠀⠀⠀
⠀⠀⠀⠛⠻⢶⢶⡶⡶⢶⡶⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀       
'''

paper = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠶⠒⠣⣦⠀⠀⠀⠀⠀
⠀⢀⣀⣀⢀⠀⠀⠀⠀⢀⡾⠃⠀⠀⣠⡟⠀⡀⠀⠀⠀
⠀⣼⠉⠈⠉⢷⡀⠀⣰⠟⠁⠀⠀⣴⣿⡶⠛⠛⠺⣦⠀
⠀⠸⣧⠀⠀⢸⣧⡾⠁⠀⠀⢀⡾⠋⠁⠀⠀⠀⣠⡾⠀
⠀⠀⣹⠀⠀⠈⠁⠀⠀⠀⢀⠊⠀⠀⠀⣠⣴⣿⣭⣀⠀
⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠋⠉⠉⢙⣷
⢠⡾⢻⠀⡠⠎⢀⡴⠀⠀⠀⠀⠐⠁⠀⢀⣠⡴⠞⠋⠁
⠀⢿⡈⢧⡀⠖⣉⡤⠆⠀⠀⠀⢀⣴⠾⠋⠁⠀⠀⠀⠀
⠀⠈⢳⣄⠱⢤⣀⣀⣀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠛⠛⠁⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
'''

scissors = '''
⠀⠀⠀⠀⠀⠀⣠⠾⠛⢶⡄⠀⠀⠀⠀
⠀⣴⠛⠺⣦⢸⡏⠀⠀⢸⡇⠀⠀⠀⠀
⢸⡇⠀⠀⢹⣿⡇⠀⠀⢸⠆⠀⠀⠀⠀
⠀⢿⡄⠀⠀⢳⡇⠀⠀⠘⣷⢀⠀⠀⠀
⠀⠈⢷⡀⠀⠀⢳⠀⠀⠀⢣⠑⢗⠄⠀
⠀⢀⣼⢧⠀⠀⠀⠁⠀⠀⠈⠀⠈⣟⡀
⠀⣿⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⢿⡀⠂⠀⠀⠀⠀⢰⠀⣀⠀⠀⣼⠃
⠀⠈⢷⣄⠀⠀⠘⡆⢸⠀⡇⠀⣰⡟⠀
⠀⠀⠀⠙⢷⣤⣀⣃⣈⣀⡥⢾⡍⠀⠀
⠀⠀⠀⠀⠈⠷⡤⡤⢤⣤⣴⠟⠁⠀⠀⠀                   
                                  
'''


# store RPS print sign in a list call option
options = [rock, paper, scissors]
# Add your code here

print("""\n\n
                                                ⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
                                                ⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
                                                ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
                                                ⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
                                                ⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀
                                                ⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
                                                ⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
                                                ⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
                                                ⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

print("""\n
    ____  ____  ________ __        ____  ___    ____  __________         _____ ____________________ ____  ____  _____
   / __ \/ __ \/ ____/ //_/       / __ \/   |  / __ \/ ____/ __ \       / ___// ____/  _/ ___/ ___// __ \/ __ \/ ___/
  / /_/ / / / / /   / ,<         / /_/ / /| | / /_/ / __/ / /_/ /       \__ \/ /    / / \__ \\__ \/ / / / /_/ /\__ \ 
 / _, _/ /_/ / /___/ /| |       / ____/ ___ |/ ____/ /___/ _, _/       ___/ / /____/ / ___/ /__/ / /_/ / _, _/___/ / 
/_/ |_|\____/\____/_/ |_|      /_/   /_/  |_/_/   /_____/_/ |_|       /____/\____/___//____/____/\____/_/ |_|/____/  
                                                                                                                     
                                                                                                                                                                                                                                                                      
""")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
print("┆      💡  💡  💡 Here are the instructions to play the ROCK PAPER SCISSORS game. ⬇️   ⬇️   ⬇️                     ┆")
print("┆                                                                                                               ┆")
print("┆     1️⃣  .Enter your name  📋  📋  📋 :                                                                         ┆")
print("┆                                                                                                               ┆")
print("┆     2️⃣  .Select one of the 3 choice. 👊 ✋ ✌️                                                                   ┆")
print("┆                                                                                                               ┆")
print("┆     3️⃣  .Each round win get 1 point. Who get 3 points first will win the game. 🥇 🥇 🥇                        ┆")
print("┆                                                                                                               ┆")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

user_name = input("📋  📋  📋 Enter your name: ")


#The first while True loop is to check if user wish to continue the game or they wish to stop
while True:
    # These two variables is to track the point for user and computer, when they win a round the point will +1
    user_point = 0
    bot_point = 0
    while True:
        try:
            if user_point == 0:
                user_point_ui = '''0️⃣'''
            elif user_point == 1:
                user_point_ui = '''1️⃣'''
            elif user_point == 2:
                user_point_ui = '''2️⃣'''
            if bot_point == 0:
                bot_point_ui = '''0️⃣'''
            elif bot_point == 1:
                bot_point_ui = '''1️⃣'''
            elif bot_point == 2:
                bot_point_ui = '''2️⃣'''
            print(f"\n🧑 {user_name}'s Point =", user_point_ui)
            print("🤖 Bot Point =", bot_point_ui)
            print("\nEnter 0 for ROCK ✊, 1 for PAPER ✋, and 2 for SCISSORS ✌️")
            user_choice = int(input("Please select your choices: "))
            # The below if code is to check with the user's input
            # The len function will check how many variable in the list (Should be 3, since there are 3 varible in list options)
            # And range here will generate a sequence of numbers from 0 to len(options) - 1, which is used to represent the indexs of the list
            # So we check if user's input is a valid index for the list
            # So if input is not a valid index then the code will print "Invalid input"
            if user_choice not in range(len(options)):
                print("Invalid input ❌")
            # But if input is in range then the code will continue to check what is the input and print out as the variable in the list base on user's input
            else:
                print(options[user_choice])
                print(f"{user_name}'s 🧑 :")
                print("\n-------------------------------------")
            # The randint function will random 3 numbers from 0,2 which is represent to Rock, Paper, Scissors same as user's choices
                bot_choice = randint(0,2)
                # Same here, as what the code check for user, we do the same to print out the choice that bot chose
                print(options[bot_choice])
                print("Bot's 🤖:")
                print("\n-------------------------------------")
                # Function Called to see who win or lose
                result = rps_match(user_choice, bot_choice)

                #These 3 below condition, is to check the returned value from the function
                
                # If the return is 1, then user will win the round and point will +1
                if result == 1:
                    print(f"🧑 {user_name} win this round ➕ 1️⃣")
                    user_point += 1
                # If the return is -1, then bot will win the round and point will +1    
                elif result == -1:
                    print("🤖 Bot win this round  ➕ 1️⃣")
                    bot_point += 1
                # But if the return is 0, then the round is Tie and no one get +1 point
                elif result == 0:
                    print("This round is Draw🤝")
                    user_point += 0
                    bot_point += 0
                # These below conditions are checking for winner
                # If someone got 3 point first, then they will win the game.
                if user_point == 3:
                    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    print(f"\n🎉 🥳 👏  Congratulation, {user_name} win 🎉 🥳 👏")
                    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    break
                elif bot_point == 3:
                    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    print("\n🤖 🎉 Bot Win 🤖 🎉")
                    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    break
        except ValueError:
            print("Invalid input ❌")
    check_continue = input('\n🔄🔄🔄 Do you want to start again? 🔄🔄🔄 y/n: ').lower()
    if check_continue != 'n':
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("\nLoading… 🔜")
        print("\n⏳ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 100% ⏳")
        print("\nRestarted🔄✅")
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        True
    else:
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("\nShutting down... 🔜")
        print("\n⏳ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 100% ⏳")
        print("\nExit⛔⛔")
        print("\nThank you for using our app 🥰 🥰 🥰")
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        break