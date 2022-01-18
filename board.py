class Board:

    def __init__(self,nrows, ncolumns):
        self.board = [[' ']*ncolumns for _ in range(nrows)]
        self._moves_done =0

    def __repr__(self):
        new_t = ''
        h = self.get_nrows()  # num_rows
        l = self.get_ncolumns() # num_columns
        new_t = new_t + '  '
        for i in range(l):
            new_t = new_t + str(i) + ' '
        new_t = new_t + '\n'
        for i in range(h):
            new_t = new_t + str(i) + '|'
            for j in range(l):
                k = self[i,j]
                new_t = new_t + str(k) + '|'
            new_t = new_t + '\n'

        return new_t

    def __getitem__(self, item):
        assert isinstance(item, tuple), 'item should be tuple'
        i,j = item
        assert i < self.get_nrows(), 'i must be smaller than num rows'

        return self.board[i][j]
        #'self[i,j]'= self.board[i][j]

    def __setitem__(self, key, value):
        i, j = key
        self.board[i][j] = value

    def get_nrows(self):
        h = len(self.board)  # num_rows
        return h

    def get_ncolumns(self):
        l = len(self.board[0])
        return l

    def result(self, win_num):
        l = self.get_nrows()  # num_rows
        h = self.get_ncolumns()  # num_columns
        w = win_num
        winner = ''
        for i in range(l):
            for j in range(h - w + 1):
                if all(self[i,j + k] == 'X' for k in range(w)) or all(self[i,j + k] == 'O' for k in range(w)):
                    winner = self[i,j]

        for i in range(l - w + 1):
            for j in range(h):
                if all(self[i + k,j] == 'X' for k in range(w)) or all(self[i + k,j] == 'O' for k in range(w)):
                    winner = self[i,j]

        for i in range(l - w + 1):
            for j in range(h - w + 1):
                if all(self[i + k,j + k] == 'O' for k in range(w)) or all(
                        self[i + k,j + k] == 'X' for k in range(w)):
                    winner = self[i,j]

        for j in range(h - w + 1):
            for i in range(l - w + 1):
                if all(self[i + k,j + w - 1 - k] == 'O' for k in range(w)) or all(
                        self[i + k,j + w - 1 - k] == 'X' for k in range(w)):
                    winner = self[i,j + w - 1]

        if winner == 'O':
            return 2
        if winner == 'X':
            return 1
        else:
            return 0

    def move(self, current_player, move):
        l = self.get_nrows()  # num_rows
        h = self.get_ncolumns()  # num_columns
        p_1, p_2 = move

        if (p_1 in range(l)) and (p_2 in range(h)) and (self[p_1,p_2] == ' '):
            if current_player == 0:
                self[p_1,p_2] = 'X'

            else:
                self[p_1,p_2] = 'O'
            self._moves_done += 1
            return True

        else:
            print("Wrong move dumbass!")
            return False

    def full(self):
        l = self.get_nrows()  # num_rows
        h = self.get_ncolumns()  # num_columns
        is_full = self._moves_done == h*l
        return is_full

if __name__=="__main__":
    b=Board(3,3)
    print(b)

    b[0,0]='O'
    b[1, 1] = 'O'
    b[2, 2] = 'O'

    print(b)
    print(b.result(3))