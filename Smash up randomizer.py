import random
# List of all factions worth playing with in the game. Removed the Munchkin series.
list_all = ['Aliens' , 'Ancient Egyptians' , 'Astro Knights' , 'Minions of Cthulhu' ,  \
            'Changebots' , 'Cowboys' , 'Cyborg Apes' , 'Dinosaurs' , 'Disco Dancers' , \
            'Dragons' , 'Elder Things' , 'Explorers' , 'Fairies' , 'Geeks' , 'Ghosts' ,\
            'Giant Ants' , 'Grannies' , 'Ignobles' , 'Innsmouth' , 'Itty Critters' ,   \
            'Kaiju' , 'Killer Plants' , 'Kitty Cats' , 'Kung Fu Fighters' , 'Megabot' ,\
            'Mad Scientists' , 'Magical Girls' , 'Bear Cavalry' , 'Mythic Greeks' ,    \
            'Miskatonic University' , 'Mythic Horses' , 'Ninjas' , 'Pirates' ,         \
            'Princesses' , 'Robots' , 'Rock Stars' , 'Samurai' , 'Steampunks' ,        \
            'Shapeshifters' , 'Sharks' , 'Sheep' , 'Smash Up All Stars' , 'Tornados' , \
            'Star Roamers' , 'Super Heroes' , 'Super Spies' , 'Teddy Bears' ,          \
            'Time Travellers' , 'Tricksters' , 'Truckers' , 'Vampires' , 'Vigilantes' ,\
            'Vikings' , 'Wizards' , 'Werewolves' , 'Zombies']

#Just an intro to the program.
print("Welcome to the Smash Up Randomizer!!!")

#Main while loop, y = ask to randomize, n = stop program.
game = str(input("Would you like to play a game, (y/n)? "))
while game != "n":
    if game == "y":
        #All this does is pick pairs of elements in the list. Doesn't do anything fancy.
        #Next I want it to remove elements from the list once selected.
        players = int(input("How many players? "))
        while players > 0 :
            decks = random.sample(list_all, k=2)
            print(decks)
            players = players - 1
    else :
        print("Did you not read the fucking directions? \nLets try this again...")
    
    game = str(input("Would you like to play a game, (y/n)? "))
print("Alright, see ya next time.")
