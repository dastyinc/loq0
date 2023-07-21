from loq0 import Game, ACTION

a = Game()
a.act(ACTION.MOVE, 5, 2)
a.act(ACTION.PLACE_L, 3, 2, 2)
a.act(ACTION.PLACE_L, 3, 2, 4)
a.act(ACTION.PLACE_I, 2, 1, 1)
a.act(ACTION.PLACE_I, 4, 2, 2)
print(a)
