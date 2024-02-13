from rps import rps_match
from random import randint

rock = '''
                          ++++++                   
                     +++ +      +                  
                   +     ++      +                 
               +++++       +     ++                
             ++     ++     ++ ++++++++++           
         +++++++      +   +++            ++        
        ++      +++    +++                +        
       ++         ++   ++                 ++       
       ++           ++ +                  ++       
        +            ++++        +        ++       
        +   +         +++ ++++++          +        
        ++   ++      +++                 ++        
         +     ++++++ +                  +         
         ++           +                 ++         
          +                            ++          
           ++                         ++           
            ++                       ++            
             ++                    +++             
               ++                ++                
                  +++++++++++++        
'''

paper = '''
                          ++++                     
                        ++    +   ++   +           
                +   ++  +     ++ ++     +          
               +     + ++      + +      +          
              ++     ++++      +++      +          
          ++   +      +++      +++      +          
        ++  ++ +      +++      +++      +          
        +     +++     +++      ++       +          
        ++    +++     +++      ++       +          
         +     +++     ++      ++      ++          
         +      ++     ++      ++      ++          
         ++      +     ++      ++      +     +++   
          +      ++ +++++++++++++      +  +++    ++
          ++   +++                    ++++        +
           ++ +                   ++++++         ++
            +                  +++             ++  
            ++               ++               ++   
             +             ++                ++    
             ++            +                ++     
              +            +                +      
               +           +               +       
               ++                         +        
                 +                       ++        
                  ++                   ++          
                   +++              +++            
                      +++++++++++++    
'''

scissors = '''
           +++++++             +++                 
          ++     ++          ++   ++               
         ++       ++        ++     ++              
         ++       ++       ++       +              
         ++        +      ++        +              
         ++        ++     ++        +              
         ++         +     +        ++              
          +         ++   ++        ++              
          +         ++   +         ++              
          ++        ++  ++        ++               
          ++         +  +         ++               
          ++         + ++         ++               
           +         ++++         +                
           ++        ++++        ++                
      +++++++++       ++        ++++               
     ++       +++     ++  ++++++++++++++           
  +++++++       ++   ++++              +++         
+++     +++      +++++                  ++         
++         +++    ++                     ++        
+            ++   ++                     ++        
+             ++  ++                     ++        
++             +++++++++   +++          ++         
++   ++         +++     +++             ++         
++     ++      ++++                    ++          
 ++      +++++++++                    ++           
 ++              +                    ++           
  ++             +                   ++            
   ++                               ++             
    ++                             ++              
     ++                           ++               
      +++                       ++                 
        ++++                ++++                   
           ++++++++   +++++++                      
                                  
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
print("┆      💡  💡  💡 Here are the instruction to play the ROCK PAPER SCISSORS game. ⬇️   ⬇️   ⬇️                      ┆")
print("┆                                                                                                               ┆")
print("┆     1️⃣  .Enter 0 for ROCK ✊, 1 for PAPER ✋, and 2 for SCISSORS ✌️                                             ┆")
print("┆                                                                                                               ┆")
print("┆     2️⃣  .Please select one of the 3 choice. 👊 ✋ ✌️                                                            ┆")
print("┆                                                                                                               ┆")
print("┆     3️⃣  .Each round win get 1 point. Who get 3 points first will win the game. 🥇 🥇 🥇                        ┆")
print("┆                                                                                                               ┆")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")


#The first while True loop is to check if user wish to continue the game or they wish to stop
while True:
    # These two variables is to track the point for user and computer, when they win a round the point will +1
    user_point = 0
    bot_point = 0
    while True:
        try:
            print("🧑 User Point =", user_point)
            print("🤖 Bot Point =", bot_point)
            user_choice = int(input("Please select your choices: "))
            # The below if code is to check with the user's input
            # The len function will check how many variable in the list (Should be 3, since there are 3 varible in list options)
            # And range here will generate a sequence of numbers from 0 to len(options) - 1, which is used to represent the indexs of the list
            # So we check if user's input is a valid index for the list
            # So if input is not a valid index then the code will print "Invalid input"
            if user_choice not in range(len(options)):
                print("Invalid input")
            # But if input is in range then the code will continue to check what is the input and print out as the variable in the list base on user's input
            else:
                print(options[user_choice])
                print("User's  🧑 :")
                print("\n-------------------------------------")
            # The randint function will random 3 numbers from 0,2 which is represent to Rock, Paper, Scissors same as user's choices
                bot_choice = randint(0,2)
                # Same here, as what the code check for user, we do the same to print out the choice that bot chose
                print(options[bot_choice])
                print("Bot's  🤖:")
                print("\n-------------------------------------")
                # Function Called to see who win or lose
                result = rps_match(user_choice, bot_choice)

                #These 3 below condition, is to check the returned value from the function
                
                # If the return is 1, then user will win the round and point will +1
                if result == 1:
                    print("User win  🧑 🧑")
                    user_point += 1
                # If the return is -1, then bot will win the round and point will +1    
                elif result == -1:
                    print("Bot win  🤖 🤖")
                    bot_point += 1
                # But if the return is 0, then the round is Tie and no one get +1 point
                elif result == 0:
                    print("Tie🤝")
                    user_point += 0
                    bot_point += 0

                # These below conditions are checking for winner
                # If someone got 3 point first, then they will win the game.
                if user_point == 3:
                    print("Congratulation, User win")
                    break
                elif bot_point == 3:
                    print("Bot Win")
                    break
                else:
                    continue
        except ValueError:
            print("Invalid Input")
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