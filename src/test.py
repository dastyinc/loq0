from loq0 import Game, ACTION

a = Game()
a.act(ACTION.MOVE, 5, 2)

a.act(ACTION.PLACE_I, 1, 8, 2)
a.act(ACTION.PLACE_I, 5, 8, 2)
a.act(ACTION.PLACE_I, 8, 9, 2)
a.act(ACTION.PLACE_I, 3, 8, 2)
a.act(ACTION.PLACE_I, 7, 8, 2)
a.act(ACTION.PLACE_I, 8, 8, 1)
print(a.st.endable())
print(a)
