class colors:
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'


def bold_sym(s: str):
    return "╋" if s == "┼" else "┃" if s == "│" else "━━━" if s == "───" else s


def __str__(self):
    if self.st[0, 2] == 0:
        (px, py), (ox, oy) = self.position(), self.position(1)
    else:
        (px, py), (ox, oy) = self.position(1), self.position()

    res = f'   {" ".join(map(lambda x: str(((x + 1) // 2) % 10) if x % 2 else " ", range(17)))}\n'

    board = [[("┼" if y % 2 else "│") if x % 2 else ("───" if y % 2 else "   ") for x in range(17)] for y in range(17)]

    board[2 * (py - 1)][2 * (px - 1)] = f'{colors.BLUE} O {colors.ENDC}'
    board[2 * (oy - 1)][2 * (ox - 1)] = f'{colors.RED} O {colors.ENDC}'

    for wall_i in self.st[2:16]:
        wx, wy, opt = wall_i
        wx = 2 * wx - 1
        wy = 2 * wy - 1
        if opt == 1:  # horizontal wall
            for ty in [wy - 1, wy, wy + 1]:
                board[ty][wx] = bold_sym(board[ty][wx])
        elif opt == 2:  # vertical wall
            for tx in [wx - 1, wx, wx + 1]:
                board[wy][tx] = bold_sym(board[wy][tx])
    for wall_l in self.st[16:]:
        wx, wy, opt = wall_l
        wx = 2 * wx - 1
        wy = 2 * wy - 1
        if opt == 1:
            for coord in [(wx - 1, wy), (wx, wy), (wx, wy - 1)]:
                tx, ty = coord
                board[ty][tx] = bold_sym(board[ty][tx])
        elif opt == 2:
            for coord in [(wx + 1, wy), (wx, wy), (wx, wy - 1)]:
                tx, ty = coord
                board[ty][tx] = bold_sym(board[ty][tx])
        elif opt == 3:
            for coord in [(wx + 1, wy), (wx, wy), (wx, wy + 1)]:
                tx, ty = coord
                board[ty][tx] = bold_sym(board[ty][tx])
        elif opt == 4:
            for coord in [(wx - 1, wy), (wx, wy), (wx, wy + 1)]:
                tx, ty = coord
                board[ty][tx] = bold_sym(board[ty][tx])

    for i, line in enumerate(board):
        res += f' {(i + 1) // 2 if i % 2 else " "}{"".join(line)}{colors.CYAN}{(i + 2) // 2 if not i % 2 else " "}{colors.ENDC}\n'

    res += f'   {"   ".join(map(lambda i: f"{colors.GREEN}{i}{colors.ENDC}", range(1, 10)))}'
    return res
