## 
#project 02
## build a two piles remove stones' game
#1. choose weather want to play
#2. human player goes first, computer player goses second
#3. human choose which pile to remove, and beagin to remove. for every round computer remove a stone from the other pile
#4. check if the pile is empty, print error, and choose a new pile
#5. the game will run over and over again, until the player choose not to play
###
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ")


computer_count=0
human_count=0
current = True
game_over= False
while int(play_str) != 0:  #judge wethear to begain the game
    pile_1=5 
    pile_2=5
    print("Start --> Pile 1:",5,"   Pile 2:",5 )   
    while not game_over: 
        if current:
            
            # use current to judge the current player
            choose_pile=input("Choose a pile (1 or 2):")
            while True:
                #choose_pile=input("Choose a pile (1 or 2):")
                choose_pile = int(choose_pile)
                if choose_pile == 1 or choose_pile == 2:  # judge the input choose pile's number is 1 or 2
                    break
               #if the input is neither 1 nor 2, try again
                print(" Pile must be 1 or 2 and non-empty. Please try again.")
                choose_pile=input("Choose a pile (1 or 2):")
            #check the pile is empty, if it is empty change another pile, and print the invalid string
            while choose_pile==1 and pile_1<1:
                print(" Pile must be 1 or 2 and non-empty. Please try again.")
                choose_pile=input("Choose a pile (1 or 2):")
            while choose_pile==2 and pile_2 <1:
                print(" Pile must be 1 or 2 and non-empty. Please try again.")
                choose_pile=input("Choose a pile (1 or 2):")
                
                 
            
            num=input(" Choose stones to remove from pile:") 
            num=int(num)
             
            while True:
                 # judge the remove number is 1, 2 or 3
                 if num ==1 or num ==2 or num ==3:
                     # if the player choose pile 1
                     if  choose_pile == 1:
                         if pile_1-num <0:
                             print(" Pile must be 1 or 2 and non-empty. Please try again.")
                             break
                             
                         else:
                             pile_1 = pile_1-num
                         
                         print(" Player -> Remove",num, "stones from pile",choose_pile)
                         print("Pile 1:",pile_1,"   Pile 2:",pile_2)
                    
                # if the player choose pile 2
                     else:
                         if pile_2-num < 0:
                             print(" Pile must be 1 or 2 and non-empty. Please try again.")
                             break
                         else:
                             
                             pile_2 = pile_2-num
                         print(" Player -> Remove",num, "stones from pile",choose_pile)
                         print("Pile 1:",pile_1,"   Pile 2:",pile_2)
                         
                     break     
                     
                 else:  # if the number is not 1, 2, or 3, try again
                    print("Invalid number of stones. Please try again.")
                    choose_pile=input(" Choose stones to remove from pile:")
           
            

#        #        
            current = False # current = flase represent human player
            
         # computer play   
        else:
            stone=1
            # if huanm player choose pile 1, then the computer choose pile 2
            if choose_pile == 1: 
                if pile_2 >0: 
                    pile_2 = pile_2 -1
                    print("Computer -> Remove", stone,"stones from pile 2")
                    print("Pile 1:",pile_1,"   Pile 2:",pile_2)
                else:
                    pile_1=pile_1-1
                    print("Computer -> Remove", stone,"stone from pile 1")
                    print("Pile 1:",pile_1,"Pile 2:",pile_2)
            # if human player choose pile 2, then the computer choose pile 1  
            else:
                if pile_1>0:
                    pile_1=pile_1 -1
                    print("Computer -> Remove", stone,"stones from pile 1")
                    print("Pile 1:",pile_1,"   Pile 2:",pile_2)
                else:
                    pile_2=pile_2-1
                    print("Computer -> Remove", stone,"stone from pile 2")
                    print("Pile 1:",pile_1,"Pile 2:",pile_2)    
                
            current = True # current = true represcent computer 
            
        
        # when the pile_1 and pile_2 both are empty, then judge who is the winner
        if pile_1 == 0 and pile_2 == 0:
                #if the current player is computer, then the computer win
            if current == True:         
                print("\nComputer wins!")
                computer_count += 1
                print("Score -> human:",human_count,"; computer:",computer_count)
                game_over=True
                # if the current player is huma, then human win   
            else:
                print("\nPlayer wins!")
                human_count +=1
                print("Score -> human:",human_count,"; computer:",computer_count)
                # count each game and print
        
                game_over = True
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")
    game_over=False
else:
   print("\nThanks for playing! See you again soon!")

