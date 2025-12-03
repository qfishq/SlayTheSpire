import deck
import locations

card_index = int(input("Select which card to play: "))
location_index = int(input("Select a location on the map to travel to: "))
print("\n\n\n")

def fight(index, loc):
    selected_card = deck.cards[index] 
    player_hp = selected_card[1]
    player_cost1 = selected_card[3][0]
    player_dmg1 = selected_card[3][1]
    player_cost2 = selected_card[4][0]
    player_dmg2 = selected_card[4][1]

    
    print("Pokemon selected: " + selected_card[0])
    print("Initial HP: " + str(selected_card[1]))

    selected_loc = locations.locs[loc] 
    loc_hp = selected_loc[1]
    loc_cost1 = selected_loc[3][0]
    loc_dmg1 = selected_loc[3][1]
    loc_cost2 = selected_loc[4][0]
    loc_dmg2 = selected_loc[4][1]

    print("Location selected: " + selected_loc[0])
    print("Initial HP: " + str(selected_loc[1]))

    print("\n\n\n")


    player_hp -= player_cost1
    loc_hp -= player_dmg1

    print("You lost " + str(player_cost1) + " HP\n")
    print("Location lost " + str(player_dmg1) + " HP\n")

    print("Your HP: " + str(player_hp))
    print("Location HP: " + str(loc_hp))

    if (loc_hp <= 0):
        print("Victory!")
        return
    if (player_hp <= 0):
        print("Defeat!")
        return

    print("\n\n\n")

    loc_hp -= loc_cost1
    player_hp -= loc_dmg1

    print("You lost " + str(loc_dmg1) + " HP\n")
    print("Location lost " + str(loc_cost1) + " HP\n")


    print("Your HP: " + str(player_hp))
    print("Location HP: " + str(loc_hp))

    if (loc_hp <= 0):
        print("Victory!")
        return
    if (player_hp <= 0):
        print("Defeat!")
        return
    

    print("\n\n\n")
    

    player_hp -= player_cost2
    loc_hp -= player_dmg2

    print("You lost " + str(player_cost2) + " HP\n")
    print("Location lost " + str(player_dmg2) + " HP\n")

    print("Your HP: " + str(player_hp))
    print("Location HP: " + str(loc_hp))

    if (loc_hp <= 0):
        print("Victory!")
        return
    if (player_hp <= 0):
        print("Defeat!")
        return
    

    print("\n\n\n")
    
    loc_hp -= loc_cost2
    player_hp -= loc_dmg2

    print("You lost " + str(loc_dmg2) + " HP\n")
    print("Location lost " + str(loc_cost2) + " HP\n")


    print("Your HP: " + str(player_hp))
    print("Location HP: " + str(loc_hp))

    if (loc_hp <= 0):
        print("Victory!")
        return
    else:
        print("Defeat!")
        return
    



fight(card_index, location_index)