tile_x = 1
tile_y = 1
travel = "You can travel: "
direction = ""

def move(direction, axis):
    if direction == "n" or direction == "e":
        axis += 1
        return axis
    elif direction == "s" or direction == "w":
        axis -= 1
        return axis
    else:
        return "Not a valid direction!"
        

def north(y):
    y += 1
    return y
def south(y):
    y -= 1
    return y
def east(x):
    x += 1
    return x
def west(x):
    x -= 1
    return x
def invalid():
    return "Not a valid direction!"


while not(tile_x == 3 and tile_y == 1):

    if tile_x == 1 and tile_y == 1:
        if (len(direction) == 0):
            print(travel + "(N)orth.")
        direction = str(input("Direction: ")).lower()

        if direction == "n":
            tile_y = move(direction, tile_y)
           # tile_y = north(tile_y)
            direction = ""
        else:
           invalid()

    if tile_x == 1 and tile_y == 2:
        if (len(direction) == 0):
            print(travel + "(N)orth or (E)ast or (S)outh.")
        direction = str(input("Direction: ")).lower()

        # 
        if direction == "n":
            tile_y = move(direction, tile_y)
            direction = ""
        elif direction == "e":
            tile_x = move(direction, tile_x)
            direction = ""
        elif direction == "s":
            tile_y = move(direction, tile_y)
            direction = ""
        else:
            invalid()


    if tile_x == 1 and tile_y == 3:
        if (len(direction) == 0):
            print(travel + "(E)ast or (S)outh.")
        direction = str(input("Direction: ")).lower()

        if direction == "s":
            tile_y = move(direction, tile_y)
            direction = ""
        elif direction == "e":
            tile_x = move(direction, tile_x)
            direction = ""
        else:
            invalid()

    if tile_x == 2 and tile_y == 1:
        if (len(direction) == 0):
            print(travel + "(N)orth.")
        direction = str(input("Direction: ")).lower()
        
        if direction == "n":
            tile_y = move(direction, tile_y)
            direction = ""
        else:
            invalid()


    if tile_x == 2 and tile_y == 2:
        if (len(direction) == 0):
            print(travel + "(S)outh or (W)est.")
        direction = str(input("Direction: ")).lower()

        if direction == "w":
            tile_x = move(direction, tile_x)
            direction = ""
        elif direction == "s":
            tile_y = move(direction, tile_y)
            direction = ""
        else:
            invalid()

    if tile_x == 2 and tile_y == 3:
        if (len(direction) == 0):
            print(travel + "(E)ast or (W)est.")
        direction = str(input("Direction: ")).lower()

        if direction == "e":
            tile_x = move(direction, tile_x)
            direction = ""
        elif direction == "w":
            tile_x = move(direction, tile_x)
            direction = ""
        else:
            invalid()


    if tile_x == 3 and tile_y == 2:
        if (len(direction) == 0):
            print(travel + "(N)orth or (S)outh.")
        direction = str(input("Direction: ")).lower()

        if direction == "n":
            tile_y = move(direction, tile_y)
            direction = ""
        elif direction == "s":
            print("Victory!")
            tile_y = move(direction, tile_y)
            direction = ""
        else:
            invalid()

    if tile_x == 3 and tile_y == 3:
        if (len(direction) == 0):
            print(travel + "(S)outh or (W)est.")
        direction = str(input("Direction: ")).lower()

        if direction == "s":
            tile_y = move(direction, tile_y)
            direction = ""
        elif direction == "w":
            tile_x = move(direction, tile_x)
            direction = ""
        else:
            invalid()
