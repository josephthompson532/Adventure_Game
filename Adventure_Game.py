# Joseph Thompson

# These top few lines of input and print statements act as an intro to the story. The user is prompted to press enter 
# to progress through the text.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Press Enter to Continue through the story...")

separator = "---------------------------------------------------------------------------------------------------------------------\n"
input(separator + "You are caught in a blizzard traveling on a open wagon through the countryside.\n\nYour \
prospects are looking dim...\n\n..when you see a castle in the distance.\n\nYou head towards it..\n")

input(separator + "You arrive at the castle freezing to the bone and cross the drawbridge\n")

input(separator + "!!!CRASHHH!!!\n")

input(separator + "The bridge has collapsed!\nA short hunchbacked man approaches you wearing a tuxedo.\n")

input(separator + "You shouldn't have come here sir. This castle offers false hope. \nA demon sleeps in this here castle.\
 Best find a way to defend\nyourself before he awakes\n")

print(separator + "The man skulks off back into the castle...\n")

# Placeholder for later adding a dictionary for room descriptions
# room_descriptions =

# Placeholder for later adding a dictionary for item descriptions
# item_descriptions =

# Nested dictionary for locations within the castle. The dictionary consists of cardinal points with
# the rooms they lead to as the key value pairs
rooms = {
    "Bridge": {"East": "Entry Way"},
    "Entry Way": {"South": "Courtyard", "East": "Living Room", "West": "Bridge", "Item": "Bloody Rag"},
    "Courtyard": {"North": "Entry Way", "Item": "Garlic"},
    "Living Room": {"North": "The Study", "South": "Dining Room", "East": "Hallway", "West": "Entry Way",
                    "Item": "Eyeball"},
    "The Study": {"South": "Living Room", "East": "Armory", "Item": "Map"},
    "Armory": {"East": "Balcony", "West": "The Study", "Item": "Stake"},
    "Balcony": {"West": "Armory", "Item": "Memoir"},
    "Dining Room": {"North": "Living Room", "East": "Kitchen", "Item": "Goblet"},
    "Kitchen": {"West": "Dining Room", "Item": "Knife"},
    "Hallway": {"West": "Living Room", "East": "Dungeon", "North": "Bedroom", "Item": "Warning Letter"},
    "Dungeon": {"West": "Hallway", "Item": "Armor"},
    "Bedroom": {"South": "Hallway"}
}

# creating a global current room variable to hold the value of the current room the user is and initializing it to the 
# games starting point
current_room = "Bridge"

# Creating a global variable to hold the value of the item that a user just picked up
picked_up_item = ""

# Creating a global list to hold the players inventory
inventory = []

# Creating a global variable to hold the user's current choice of whether to exit or not
exit = False

# Global boolean to keep track of if the user is moving or Searching
moving = True

# Global boolean to keep track of if the user has won.
Winner = False

# Create a function to show the users current status 
def show_instructions():
    # call the searchResults function to return whether the user has a new item if he just tried to pick one 
    # up in the previous turn
    searchResults()
    # If the user has collected all ten items exit the function with return
    if len(inventory) == 10:
        return
    # print the users current status including his location and the directions he can move in as well as his inventory
    else: 
        print(bcolors.WARNING + "STATUS:\nYour current location is the {} and you can move in these directions: \
        {}".format(current_room, [room for room in list(rooms[current_room].keys()) if room != "Item"]))
        print("Inventory: {}".format(inventory))

# Create a function to keep track of the results of the "checking_for_item" function and print out a message 
# in the following show_instructions call if there was an item found. If there was no item found print no item 
# found and print nothing if the user didn't search and only moved.
def searchResults():
    # declare the variable as global
    global picked_up_item
    # if the variable is none, inform the user there was no item found
    if picked_up_item == "none":
        print("There are no items here\n")
        picked_up_item = ""
    # if the variable is not empty, let teh user know which item he picked up
    elif picked_up_item != "":
        print("You picked up a {}!\n".format(picked_up_item))
        picked_up_item = ""
    # if the varialbe pickup_up_item was set to an empty string by the checking_for_item function, this function
    # will simply print nothing when called
    

# this function gets input from the user
def get_user_input():
    # declare the exit, Winner, and current_room variable to be global. This function may alter both of these variables globally
    global exit
    global Winner
    global current_room
    # if the user has collected all ten items, set the global winner variable to true and exit this function.
    if len(inventory) == 10:
        Winner = True
        return
    # get input from the user for their choice about what to do. Include instructions
    choice = input(
        "Which way would you like to go?\n\nInput either a direction, 'Search', or 'Exit' if you would like to quit the game: ").strip().title()
    # Handle all of the valid and invalid user input. If the input is invalid. prompt the user for input again/show instructions
    while (choice not in list(rooms[current_room].keys()) and not choice == "Search" and not choice == "Exit"):
        print(separator)
        print("Invalid input. Try again:\n")
        show_instructions()
        choice = input("\nInput either a direction, 'Search', or 'Exit' if you would like to quit the game: ").strip().title()
    
    # if choice is to search, call the checking_for_item functions
    if choice == "Search":
        checking_for_item()
    
    # if the choice is to exit the game, exit this function with a return statement
    if choice == "Exit":
        exit = True
        return
    
    # if the choice is within the list of valid directions for the current room, set the current room to 
    # the room that corresponds to the users choice for the current room in the rooms dictionary.
    if choice in list(rooms[current_room].keys()):
        print("You are moving from room {} to room {}".format(current_room, choice))
        current_room = rooms[current_room][choice]


# create a function for run when the user selects "Search" in the "get_user_input" function
def checking_for_item():
    # make the picked_up_item variable global in the scope of this function
    global picked_up_item
    # print a message to the user 
    print("checking for item...")
    # if the key "Item" is in the dictionary that corresponds to the current "current_room" variable (the room the user
    # is in at this point in the game) assign it to the "item" variable.
    if "Item" in rooms[current_room]:
        item = rooms[current_room]["Item"]
        # assign the value of 'item' to the inventory list. do not need to make inventory global because it is a list
        inventory.append(item)
        # delete the key: item from the dictionary
        del rooms[current_room]["Item"]
        # assign picked_up_item to the item value
        picked_up_item = item
    # if "item" is not a key in the dictionary, set picked_up_item equal to none
    else:
        picked_up_item = "none"
    

# This while loop is what keeps the game running. Loop until the users current room is "Bedroom", Winner=True, or 
# exit = True. 
while not exit:
    # print the separator for aesthetic purposes
    print(separator)
    show_instructions()
    get_user_input()
    # if the user enters the bedroom he has lost. Print out corresponding messages
    if current_room == "Bedroom":
        print(separator)
        print("OHHH MY GOOOOOOD!")
        print("\n*You walked right into the vampires lair. He grabs you and sucks out all of your blood until you are nothing but a dry husk.")
        print("\nGame Over. You lose.")
        break
    # if Winner is equal to True, that means it was set to True in the get_user_input function because the user has
    # collected all ten items. Print out that the user has collected all the items and killed the vampire. exit the 
    # loop with break
    if Winner == True:
        print("You collected enough weapons that you walked straight into the vampires bedroom and staked him through his heart!")
        print("\nYou Win!")
        break 
    # if exit is true that means the user input exit as choice and wants to exit. Let the user know they have exited
    # and exit the loop (and game) with break
    if exit:
        print("\nYou have exited the game.")
        break

