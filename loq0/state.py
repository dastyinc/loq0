import numpy as np
from .const import BOARD_SIZE, I_COUNT, L_COUNT


class State:
    def __init__(self, state=np.zeros((2 + (I_COUNT + L_COUNT) * 2, 3), dtype=np.uint8)):
        self._st = state
        self._st[0, 0] = (BOARD_SIZE + 1) // 2
        self._st[0, 1] = 1
        self._st[1, 0] = (BOARD_SIZE + 1) // 2
        self._st[1, 1] = BOARD_SIZE

    def copy(self):
        return State(self._st.copy())

    def player(self):
        return self._st[0, 2]

    def opponent(self):
        return 1 - self._st[0, 2]

    def internal(self):
        pl = self.player()
        return 4 <= self._st[pl, 0] <= 6 and 4 <= self._st[pl, 1] <= 6

    def internal_opponent(self):
        pl = 1 - self.player()
        return 4 <= self._st[pl, 0] <= 6 and 4 <= self._st[pl, 1] <= 6

    def i_walls(self):
        idx = np.where(self._st[2:2 + I_COUNT * 2, 0] != 0)[0] + 2
        return self._st[2:idx, :]

    def l_walls(self):
        idx = np.where(self._st[2 + I_COUNT * 2:, 0] != 0)[0] + 2 + I_COUNT * 2
        return self._st[2 + I_COUNT * 2:idx, :]

    def position(self):
        pl = self.player()
        return (self._st[pl, 0], self._st[pl, 1]), (self._st[1 - pl, 0], self._st[1 - pl, 1])

    from validate.blocked import horizontal_block, vertical_block
    from validate.movable import movable

    from validate.endable import endable
