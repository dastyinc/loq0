from .state.state import State


class Game:
    def __init__(self, state=None):
        self.st = State(state)

    def copy(self):
        return Game()

    def player(self, op=None):
        return self.st.player(op)

    def act(self, action, *args):
        ret = self.st.act(action, *args)
        if ret is False:
            return False
        self.st = ret

    def __str__(self):
        return self.st.__str__()
