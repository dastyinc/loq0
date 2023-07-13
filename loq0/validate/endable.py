import numpy as np
from ..const import BOARD_SIZE, I_COUNT, L_COUNT

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(self, stk, pl):
    visited = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=bool)
    visited[stk[0][0], stk[0][1]] = True
    while len(stk) > 0:
        x, y = stk.pop()
        for i in range(1, 5):
            if not visited[x + dx[i] - 1, y + dy[i] - 1] and self.movable((x + dx[i], y + dy[i]),
                                                                          self.position()[0]):
                if pl == 0 and x + dx[i] == BOARD_SIZE:
                    return True
                elif pl == 1 and y + dy[i] == BOARD_SIZE:
                    return True
                visited[x - 1, y - 1] = True
                stk.append((x + dx[i], y + dy[i]))

    return False


def endable(self):
    return bfs([self.position()[0]], self.player()) and self._bfs([self.position()[1]], 1 - self.player())
