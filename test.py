from loq0 import State, ACTION_MOVE, ACTION_PLACE_I, ACTION_PLACE_L

a = State()
a = a.act(ACTION_MOVE, 5, 2)
a = a.act(ACTION_PLACE_L, 3, 2, 2)
a = a.act(ACTION_PLACE_L, 3, 2, 4)
a = a.act(ACTION_PLACE_I, 2, 1, 1)
a = a.act(ACTION_PLACE_I, 4, 2, 2)
print(a)
