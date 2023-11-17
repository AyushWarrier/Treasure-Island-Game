print("Welcome to Tresure Island.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()
print(f"You choose to go {direction}")
if direction == 'left':
    step = input("You came to a lake. There is an island in view in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if step == 'wait':
        door = input("A Boat comes hit the shore after waiting a while. You sat in the boat and reached the island. Now you have 3 Doors in front of you. RED, BLUE and GREEN. Choose ").upper()
        if door == 'RED':
            print("You walked into hell and became DEVIL's Food")
        elif door == 'BLUE':
            print("You found HEAVEN and are going to live good")
        elif door == 'GREEN':
            print('You earn a HAREM')
        else:
            print("Your BLIND or a DUMBFUCK")
    elif step == 'swim':
        print("Bruhh you got eaten till there were only bones by Piranhas *Not_the_Best_choice*")
    else:
        print("STOOPID")
elif direction == 'right':
    print("You stepped on a landmine and blew up @__@")    
else:
    print("LEFT or RIGHT brooooooo")