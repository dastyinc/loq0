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
        return (self._st[0, 0], self._st[0, 1]), (self._st[1, 0], self._st[1, 1])

    def _move(self, pos):
        x, y = pos
        if x < 1 or x > BOARD_SIZE or y < 1 or y > BOARD_SIZE:
            return False
        dis = abs(self._st[self.player(), 0] - x) + abs(self._st[self.player(), 1] - y)
        if dis > 2 or dis == 0:
            return False
        elif dis == 1:
            if x == self._st[self.player(), 0]:
                if self.vertical_block(x, min(y, self._st[self.player(), 1])):
                    return False
            elif self.horizontal_block(min(x, self._st[self.player(), 0]), y):
                return False
        else:
            if x == self._st[self.player(), 0]:
                yt = self._st[self.opponent(), 1]
                if self._st[self.opponent(), 0] != x or yt * 2 != y + self._st[self.player(), 1]:
                    return False
                if self.vertical_block(x, yt) or self.vertical_block(x, yt + 1):
                    return False
            elif y == self._st[self.player(), 1]:
                xt = self._st[self.opponent(), 0]
                if self._st[self.opponent(), 1] != y or xt * 2 != x + self._st[self.player(), 0]:
                    return False
                if self.horizontal_block(xt, y) or self.horizontal_block(xt + 1, y):
                    return False
            elif self._st[self.player(), 0] == self._st[self.opponent(), 0] and y == self._st[self.opponent(), 1]:
                if abs(x - self._st[self.player(), 0]) != 1 or \
                        self.vertical_block(self._st[self.player(), 0], min(y, self._st[self.player(), 1])) or \
                        self.horizontal_block(min(x, self._st[self.player(), 0]), y) or \
                        not self.vertical_block(self._st[self.player(), 0],
                                                y + 1 if y > self._st[self.player(), 1] else y - 1):
                    return False
            elif self._st[self.player(), 1] == self._st[self.opponent(), 1] and x == self._st[self.opponent(), 0]:
                if abs(y - self._st[self.player(), 1]) != 1 or \
                        self.vertical_block(x, min(y, self._st[self.player(), 1])) or \
                        self.horizontal_block(min(x, self._st[self.player(), 0]), y) or \
                        not self.horizontal_block(x + 1 if x > self._st[self.player(), 0] else x - 1,
                                                  self._st[self.player(), 1]):
                    return False
            else:
                return False

        if self._st[self.opponent(), 0] == x and self._st[self.opponent(), 1] == y and not self.internal():
            return False

        return True
