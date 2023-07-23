from loq0 import Game, ACTION

game = Game()
print(game)

while True:
    a = input(f'{"red turn action: " if game.player() else "blue turn action: "}').split()
    t = a[0]
    x = int(a[1])
    y = int(a[2])
    if len(a) == 4:
        w = int(a[3])

    if t == 'M':
        r = game.act(ACTION.MOVE, x, y)
    elif t == 'I':
        r = game.act(ACTION.PLACE_I, x, y, w)
    elif t == 'L':
        r = game.act(ACTION.PLACE_L, x, y, w)

    if r is None:
        print("You Died")
        break
    elif not r:
        print("Invalid")
        break
    else:
        print(game)
