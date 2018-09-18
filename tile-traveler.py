#við viljum byrja á að gera while setningu, sem heldur utan um að á meðan staðsetningin er ekki 3,1 þá heldur leikurinn áfram
#við getum gert if loopur til að halda utan um reglurnar fyrir hverja flís

#x=1
#y=1
#while location != 3,1:
    #print options_available
    #input()
    #if input == options_available
        #location== new
    #else:
        #print invalid option
#else: print("you won!")

tile_x = 1
tile_y = 1
location = tile_x, tile_y
travel = "You can travel: "
        

while tile_x != 3 and tile_y != 1:

    if tile_x == 1 and tile_y == 1:
        print(travel + "(N)orth")
        direction = str(input("Direction: ")).lower
        if direction == "n":
            tile_x += 1
            location == 12
        else:
            print("Not a valid direction!")

    if location == 12:

        print(travel + "(N)orth or (E)ast or (S)outh.")
        direction = str(input("Direction: ")).lower
        if direction == "N":
            location == 13
        elif direction == "E":
            location == 21
        elif direction == "S":
            location == 11
        else:
            print("Not a valid direction!")
    



