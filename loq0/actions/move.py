def move(self, x, y):
    if not self.movable((x, y)): return False
    st = self.copy()
    pl = st.player()
    st.st[pl, 0] = x
    st.st[pl, 1] = y
    st.st[pl, 2] = 1 - pl
    return st