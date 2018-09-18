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
direction = ""


#if tile_x == 3 and tile_y == 1:
 #   print("Victory!")


while not(tile_x == 3 and tile_y == 1):

    if tile_x == 1 and tile_y == 1:
        if (len(direction) == 0):
            print(travel + "(N)orth.")
        direction = str(input("Direction: ")).lower()

        if direction == "n":
            tile_y += 1
            direction = ""
        else:
           print("Not a valid direction!")

    if tile_x == 1 and tile_y == 2:
        if (len(direction) == 0):
            print(travel + "(N)orth or (E)ast or (S)outh.")
        direction = str(input("Direction: ")).lower()

        if direction == "n":
            tile_y += 1
            direction = ""
        elif direction == "e":
            tile_x += 1
            direction = ""
        elif direction == "s":
            tile_y -= 1
            direction = ""
        else:
            print("Not a valid direction!")


    if tile_x == 1 and tile_y == 3:
        if (len(direction) == 0):
            print(travel + "(E)ast or (S)outh.")
        direction = str(input("Direction: ")).lower()

        if direction == "s":
            tile_y -= 1
            direction = ""
        elif direction == "e":
            tile_x += 1
            direction = ""
        else:
            print("Not a valid direction!")

    if tile_x == 2 and tile_y == 1:
        if (len(direction) == 0):
            print(travel + "(N)orth.")
        direction = str(input("Direction: ")).lower()
        
        if direction == "n":
            tile_y += 1
            direction = ""
        else:
            print("Not a valid direction!")


    if tile_x == 2 and tile_y == 2:
        if (len(direction) == 0):
            print(travel + "(S)outh or (W)est.")
        direction = str(input("Direction: ")).lower()

        if direction == "w":
            tile_x -= 1
            direction = ""
        elif direction == "s":
            tile_y -= 1
            direction = ""
        else:
            print("Not a valid direction!")

    if tile_x == 2 and tile_y == 3:
        if (len(direction) == 0):
            print(travel + "(E)ast or (W)est.")
        direction = str(input("Direction: ")).lower()

        if direction == "e":
            tile_x += 1
            direction = ""
        elif direction == "w":
            tile_x -= 1
            direction = ""
        else:
            print("Not a valid direction!")


    if tile_x == 3 and tile_y == 2:
        if (len(direction) == 0):
            print(travel + "(N)orth or (S)outh.")
        direction = str(input("Direction: ")).lower()

        if direction == "n":
            tile_y += 1
            direction = ""
        elif direction == "s":
            print("Victory!")
            tile_y -= 1
            direction = ""
        else:
            print("Not a valid direction")

    if tile_x == 3 and tile_y == 3:
        if (len(direction) == 0):
            print(travel + "(S)outh or (W)est.")
        direction = str(input("Direction: ")).lower()

        if direction == "s":
            tile_y -= 1
            direction = ""
        elif direction == "w":
            tile_x -= 1
            direction = ""
        else:
            print("Not a valid direction")




