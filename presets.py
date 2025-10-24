def choose_preset(game,sim):
    if sim == 1:
        choice = -1
        while choice not in range(0,4):
            choice = int(input("Choose a preset: \n1. A skinny guy and a not so skinny guy (1:1) \n2. A car and a container (1000:1)\n3. 1 Liter and 1 Gallon of Water (1:20) \nI choose "))
        return choice
    if sim == 2 or sim == 3:
        choice = -1
        while choice not in range(0,4):
            choice = int(input("Choose a preset: \n1. Moon and Earth \n2. A car and a container (1000:1)\n3. 1 Liter and 1 Gallon of Water (1:20) \nI choose "))
        return choice
    return None
def load_presets(game,sim,choice):
    if sim == 1:
        match choice:
            case 1:
                game.scale = 1
                game.c1.m = 50
                game.c2.m = 200
            case 2:
                game.scale = 1000
                game.c1.m = 2000
                game.c2.m = 30000
            case 3:
                game.scale = .05
                game.c1.m = 1
                game.c2.m = 3.78

    elif sim == 2 or sim == 3:
        match choice:
            case 1:
                game.scale = 100000
                game.ini_v = -0.1
                game.c1.m = 5_000_000
                game.c2.m = 10_000_000






