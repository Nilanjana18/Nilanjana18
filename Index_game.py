#indexgame

def user_choice():
            
    choice="WRONG"
    acceptable_values=range(0,11)
    print(list(acceptable_values))
    
    while choice.isdigit()==False or int(choice) not in acceptable_values:
        choice=input("Please enter a number (0-10): ")
        print("\n")
        
        if choice.isdigit()==False:
            print("Sorry that is not a digit")
            print("\n")
        if choice.isdigit()==True:
            if int(choice) not in acceptable_values:
                print('Enter the number within the specified range ')
                print("\n")
            
    return int(choice)

game_list=[0,1,2]
def display_game(game_list):
            print('Here is the list of indices: ')
            print("\n")
            print(game_list)
            print("\n")

def position_choice():
            
    choice ='wrong'
    
    while choice not in ['0','1','2']:
        choice=input("Pick a position (0,1,2): ")
        print("\n")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
            print("\n")
            
    return int(choice)

def replacement_choice(game_list,position):
            
    user_placement=input("Type a string to place at choosed position: ")
    print("\n")
    
    game_list[position]=user_placement
    
    return game_list

def gameon_choice():
            
    choice="Wrong"
    
    while choice not in ['Y','N']:
        
        choice=input("Keep playing? (Y or N) ")
        print("\n")
        if choice not in ['Y','N']:
            print('Sorry, invalid choice!')
            print("\n")
    
    if choice=="Y":
        return True
    else:
        return False
     
game_on=True
game_list=[0,1,2]

while game_on:
    
    display_game(game_list)
    
    position=position_choice()
    
    game_list=replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on=gameon_choice()
