from loq0 import State, ACTION_MOVE, ACTION_PLACE_I, ACTION_PLACE_L

a = State()
a = a.act(ACTION_MOVE, 5, 2)
print(a)
a = a.act(ACTION_PLACE_L, 3, 3, 1)
print(a)
