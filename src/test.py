from loq0 import Game, ACTION

a = Game()
a.act(ACTION.MOVE, 5, 2)

a.act(ACTION.PLACE_I, 1, 8, 2)
a.act(ACTION.PLACE_I, 5, 8, 2)
a.act(ACTION.PLACE_I, 8, 9, 2)
a.act(ACTION.PLACE_I, 3, 8, 2)
a.act(ACTION.PLACE_I, 7, 8, 2)
if a.act(ACTION.PLACE_I, 8, 8, 1):
    raise Exception("Should not be able to place I")

a = Game()
a.act(ACTION.PLACE_I, 8, 7, 2)
a.act(ACTION.PLACE_I, 9, 5, 1)
if a.act(ACTION.PLACE_I, 7, 7, 2):
    raise Exception("Should not be able to place I")

a = Game()
a.act(ACTION.PLACE_I, 8, 7, 2)
a.act(ACTION.PLACE_I, 8, 5, 1)
if not a.act(ACTION.PLACE_I, 8, 6, 2):
    raise Exception("Should be able to place I")

a = Game()
a.act(ACTION.MOVE, 5, 2)
a.act(ACTION.MOVE, 5, 8)
a.act(ACTION.MOVE, 5, 3)
a.act(ACTION.MOVE, 5, 7)
a.act(ACTION.MOVE, 5, 4)
a.act(ACTION.MOVE, 6, 7)
a.act(ACTION.MOVE, 5, 5)
a.act(ACTION.MOVE, 5, 7)
a.act(ACTION.MOVE, 5, 6)
a.act(ACTION.MOVE, 5, 6)
print(a)