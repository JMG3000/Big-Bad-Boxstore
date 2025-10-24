"""
File Name: BigBadBoxStore.py
Written by: JakeTheSnake(JMG3000)

This is a simple text based game that uses keyboard input to move and gather items.

To-Do:
-Add a map in the comments.

"""


#function to show instructions
def show_instructions():
    #print a main menu and the commands
    print("Big, Bad Boxstore Text Adventure Game")
    print("Stock 6 items to win the game, or be fired by the boss.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: stock 'box name'")


#function to show the player's current room, inventory of stocked boxes, and if there is a box in the current room
def show_status(current_room, boxes_stocked,rooms):
    print(f'\nYou are in the {current_room}.')
    print(f'Boxes stocked: {boxes_stocked}')

    #checks if there is a box to be stocked
    if 'Box' in rooms[current_room]:
        print(f"You see a box of {rooms[current_room]['Box']}")

    print('-----------')

#function to move from room to room
def make_move(direction, rooms, current_room):
    if direction in rooms[current_room]:

        # move in the direction that the player specified in the 'command' string to the new room
        current_room = rooms[current_room][direction]

        # this last else loop executes when an invalid direction was typed into the 'command' string
    else:

        print('You cannot go that way!')
    return current_room
    # end if loop

def main():
    #the dictionary 'rooms' states which rooms links to other rooms.
    rooms = {
        'Registers' : { 'East' : 'Dry Grocery' },
        'Dry Grocery' : { 'West' : 'Registers', 'East' : 'Clothing', 'North' : 'HBA', 'South' : 'Produce', 'Box' : 'Beans' },
        'HBA' : { 'East' : 'Automotive', 'South' : 'Dry Grocery', 'Box' : 'Shampoo' },
        'Automotive' : {'West' : 'HBA', 'Box' : 'Oil'},
        'Produce' : {'North' : 'Dry Grocery', 'East' : 'Dairy', 'Box' : 'Beets'},
        'Dairy' : {'West' : 'Produce', 'Box' : 'Milk'},
        'Clothing' : {'West' : 'Dry Grocery', 'North' : 'Office', 'Box' : 'Shoes'},
        'Office' : { 'South' : 'Clothing', 'Box' : 'Big, Bad Boss' } #villain
    }

    # empty list for the boxes that are stocked
    boxes_stocked =[]

    #sentienial value used to check for the win condition
    required_boxes = 6

    #initalizes the current room string with player in the Great Hall with no items
    current_room = 'Registers'

    #shows the player instructions
    show_instructions()

    #sets the boolean gameplay_play variable to True so that the game while run
    gameplay_loop = True

    #gameplay loop that is a while loop that runs until the player types 'exit'
    while gameplay_loop:

        #displays the current room the player is in everytime the loop runs
        show_status(current_room, boxes_stocked, rooms)


        #prompt the player for input as the string 'command'
        command= input('Enter your move: ').strip()

        #check the command string for 'exit' when the player wants to exit
        if command.lower() == 'exit':

            print('You have chosen to exit. Tootles!')

            #sets the boolean gameplay_loop variable to false so that the game will end
            gameplay_loop = False

        #check the command string for the word 'go' for when to player wants to move rooms
        elif command.lower().startswith('go '):

            #this line extracts the direction from the command string at the third index of the string
            direction = command[3:].capitalize()

            #check that the direction is valid for the current room
            current_room = make_move(direction, rooms, current_room)

        #check the command string for the word 'get'
        elif command.lower().startswith('stock '):

            box = command[6:].capitalize()

            #loop to check if there is a box in the room that needs to be stocked
            if 'Box' in rooms[current_room] and rooms[current_room]['Box'] == box:
                boxes_stocked.append(box)
                print(f"{box} has been stocked!")
                del rooms[current_room]['Box']  # Remove item from the room

            #executes when the player tries to stock the wrong box
            else:
                print("There is no such box here!")
            #end if loop

        #if there is anything else typed in as a command
        else:

            print('Invalid command.')
        #end if loop

        # Check win condition
        if current_room == 'Office' and len(boxes_stocked) == required_boxes :
            print("\nCongratulations! You have collected stocked all of the boxes and pleased the Big, Bad Boss!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            gameplay_loop = False
        #end if loop

        # Check lose condition
        elif 'Box' in rooms[current_room] and rooms[current_room]['Box'] == 'Big, Bad Boss':
            print("\nYou are fired!...GAME OVER!")
            print("Thanks for playing the game. I hope you enjoyed it.")
            gameplay_loop = False
        #end if loop

    #end while loop

#run the game
if __name__ == '__main__':
    main()