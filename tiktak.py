import random
def name():
    #here we take name input of both the players
    name.first_player = input("Player 1 Please enter your name - ")
    name.second_player = input("Player 2 Please enter your name - ")
    player_choice(name.first_player,name.second_player)# we pass the information to other function
def what_to_replay(choice):
    if choice == "YES":
        name()
    else:
        print("\nGood Bye")
def player_choice(first_player,second_player):
    while (True):
        print("\nWelcome {} and {} \n\n\t HEY {}".format(first_player,second_player,first_player))
        playerchoice = input("\nPlease enter: \n1. to choose X  or \n2. to choose O as your sign = ")# we are taking the choice of the player in a variable and then appointing them the signs as per their choice
        if playerchoice == "1":
            player_choice.first_player_choice = "X"
            player_choice.second_player_choice = "O"
            break
        elif playerchoice == "2":
            player_choice.first_player_choice= "O"
            player_choice.second_player_choice= "X"
            break
        else:
            #if the input anything else then if will throwback them to starting
            print("wrong input please retry \n\n")
            continue
        
    print("\n{} is {} and {} is {}".format(first_player,player_choice.first_player_choice,second_player,player_choice.second_player_choice)) # printing the player name with their signs which they choose 
    play_game()# issueing the next function to start the game
def play_game():
    print("\n\t LETS START THE GAME - \n")
    print("See the Table below & then choose the position wisely where to place your mark \n")
    print("""
            0  |   1   |  2
           ----|-------|-----
            3  |   4   |  5
           ----|-------|-----
            6  |   7   |  8  """)# we give them the table overview with the position where they can insert there signs , here we only want them to enter the positon anything else will be considered an wrong input or not in the range 
    
    
    position_list = ["0","1","2","3","4","5","6","7","8"]   #we will be using this list in the while loop to keep users away from using the same position again and again and if they do so they will get a message that that poisiton is already taken     
    play_game.table_list = ["0","1","2","3","4","5","6","7","8"]#this list will help in showing the position after the player enters their choice 
    one_result_check_list = [] # here we keep track of all the inputs given by the first player  and second player we will use it to compare it with the result set
    sec_result_check_list = []
    win = 0
    count=random.randint(0,9) # we use the count to keep track of which of the player is assigned the chance 
    while(position_list):
        if (count%2==0) :
            first_input = input("\nHey {} it is your turn: ".format(name.first_player))
            if first_input in position_list:#if incase the position is not taken
                count += 1#increase the count so that the chance is shifted to other player
                one_result_check_list.insert(int(first_input),int(first_input))#saving the list for the comparision with the result list 
                position_list.remove(first_input)#removing the place holder so other player cant access the same position
                play_game.table_list.pop(int(first_input)) #removing the element and addign X or O
                play_game.table_list.insert(int(first_input),player_choice.first_player_choice)
                table()
                if check_result(one_result_check_list):#result check 
                    print("\n\n\t\t\tCONGO {} you win".format(name.first_player))
                    win = 1
                    break
            
            else:
                print("that position is not there or already taken \nPlease re-enter:")
                continue
        
        elif (count%2) != 0 :
            first_input = input("\nHey {} it is your turn: ".format(name.second_player))
            if first_input in position_list:
                count += 1
                sec_result_check_list.insert(int(first_input),int(first_input))
                position_list.remove(first_input)
                play_game.table_list.pop(int(first_input))    
                play_game.table_list.insert(int(first_input),player_choice.second_player_choice)
                table()
                if check_result(sec_result_check_list):
                    print("\n\n\t\t\tCONGO {} you win".format(name.second_player))
                    win = 1
                    break
                
            else:
                print("that position is not there or  already taken \nPlease re-enter:")
                continue
    if win == 0:
        print("\n\n\tIt's a TIE")
    choice_input = input("\nIf you want to play again then type YES else type NO: ")
    choice_input = choice_input.upper()
    what_to_replay(choice_input)
        
def table ():
    final_list = play_game.table_list
    print("""
            {}  |   {}   |  {}
           ----|-------|-----
            {}  |   {}   |  {}
           ----|-------|-----
            {}  |   {}   |  {}  """.format(*final_list))
def check_result(a):
    result_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]#all the list of position that can be a winner
    a.sort()
    #we need to check if atleast 3 elements in the list a is present in any of the set of list in the result_list
    for each_list in result_list:
        if  len(a)==3:#all element of list a is in list each_list
            if all(item in each_list for item in a):
                return True
        elif len(a)>3 and len(a)<6:#all element of list each_list in list a
            if all(item in a for item in each_list):
                return True
name()

        
