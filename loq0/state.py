import numpy as np
from .const import BOARD_SIZE, I_COUNT, L_COUNT


class State:
    def __init__(self, state=np.zeros((2 + (I_COUNT + L_COUNT) * 2, 3), dtype=np.int8)):
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
        return 4 <= self._st[0, 0] <= 6 and 4 <= self._st[0, 1] <= 6

    def internal_opponent(self):
        return 4 <= self._st[1, 0] <= 6 and 4 <= self._st[1, 1] <= 6

    def i_walls(self):
        idx = np.where(self._st[2:2 + I_COUNT * 2, 0] != 0)[0] + 2
        return self._st[2:idx, :]

    def l_walls(self):
        idx = np.where(self._st[2 + I_COUNT * 2:, 0] != 0)[0] + 2 + I_COUNT * 2
        return self._st[2 + I_COUNT * 2:idx, :]

    def vertical_block(self, x, y):
        for i in range(2, 2 + I_COUNT * 2):
            if self._st[i, 1] == y and (self._st[i, 0] == x or self._st[i, 0] == x - 1) and self._st[i, 2] == 2:
                return True

        for i in range(2 + I_COUNT * 2, 2 + (I_COUNT + L_COUNT) * 2):
            if self._st[i, 2] == 1 and self._st[i, 0] == x and self._st[i, 1] == y:
                return True
            if self._st[i, 2] == 2 and self._st[i, 0] == x and self._st[i, 1] == y - 1:
                return True
            if self._st[i, 2] == 3 and self._st[i, 0] == x and self._st[i, 1] == y - 1:
                return True
            if self._st[i, 2] == 4 and self._st[i, 0] == x and self._st[i, 1] == y:
                return True

        return False

    def horizontal_block(self, x, y):
        for i in range(2, 2 + I_COUNT * 2):
            if self._st[i, 0] == x and (self._st[i, 1] == y or self._st[i, 1] == y - 1) and self._st[i, 2] == 1:
                return True

        for i in range(2 + I_COUNT * 2, 2 + (I_COUNT + L_COUNT) * 2):
            if self._st[i, 2] == 1 and self._st[i, 0] == x and self._st[i, 1] == y:
                return True
            if self._st[i, 2] == 2 and self._st[i, 0] == x and self._st[i, 1] == y:
                return True
            if self._st[i, 2] == 3 and self._st[i, 0] == x - 1 and self._st[i, 1] == y:
                return True
            if self._st[i, 2] == 4 and self._st[i, 0] == x - 1 and self._st[i, 1] == y:
                return True

        return False

    def position(self):
        pl = self.player()
        return (self._st[pl, 0], self._st[pl, 1]), (self._st[1 - pl, 0], self._st[1 - pl, 1])

    def _move(self, pos, ppos=None, opos=(0, 0)):
        x, y = pos
        if not ppos:
            (px, py), (ox, oy) = self.position()[0]
        else:
            px, py = ppos
            ox, oy = opos
        if x < 1 or x > BOARD_SIZE or y < 1 or y > BOARD_SIZE:
            return False
        dis = abs(px - x) + abs(py - y)
        if dis > 2 or dis == 0:
            return False
        elif dis == 1:
            if x == px:
                if self.vertical_block(x, min(y, py)):
                    return False
            elif self.horizontal_block(min(x, px), y):
                return False
        else:
            if x == px:
                yt = oy
                if ox != x or yt * 2 != y + py:
                    return False
                if self.vertical_block(x, yt) or self.vertical_block(x, yt + 1):
                    return False
            elif y == py:
                xt = ox
                if oy != y or xt * 2 != x + px:
                    return False
                if self.horizontal_block(xt, y) or self.horizontal_block(xt + 1, y):
                    return False
            elif px == ox and y == oy:
                if abs(x - px) != 1 or \
                        self.vertical_block(px, min(y, py)) or \
                        self.horizontal_block(min(x, px), y) or \
                        not self.vertical_block(px,
                                                y + 1 if y > py else y - 1):
                    return False
            elif py == oy and x == ox:
                if abs(y - py) != 1 or \
                        self.vertical_block(x, min(y, py)) or \
                        self.horizontal_block(min(x, px), y) or \
                        not self.horizontal_block(x + 1 if x > px else x - 1, py):
                    return False
            else:
                return False

        if ox == x and oy == y and not self.internal():
            return False

        return True

    def _endable(self):
        visited = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=bool)
        stk = [self.position()[0]]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visited[stk[0][0], stk[0][1]] = True
        while len(stk) > 0:
            x, y = stk.pop()
            for i in range(1, 5):
                if not visited[x + dx[i] - 1, y + dy[i] - 1] and self._move((x + dx[i], y + dy[i]), self.position()[0]):
                    if self.player() == 0 and x + dx[i] == BOARD_SIZE:
                        return True
                    elif self.player() == 1 and y + dy[i] == BOARD_SIZE:
                        return True
                    visited[x - 1, y - 1] = True
                    stk.append((x + dx[i], y + dy[i]))

        return False
