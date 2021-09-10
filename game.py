import copy


class Tetris:

    def __init__(self, width, height):
        self.piece = None
        self.width = width
        self.height = height
        self.position = 0
        self.frozen = False
        self.gameOver = False
        self.board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            self.board.append(row)
        self.show()

    def add_piece(self, piece):
        self.piece = copy.deepcopy(piece)
        self.position = 0
        self.frozen = False
        self.show()

    def show(self):
        if self.piece is None:
            board = self.board
        else:
            board = copy.deepcopy(self.board)
            for i in self.piece[self.position]:
                board[i // self.width][i % self.width] = 1
        for i in board:
            presentation = ["-" if x == 0 else "0" for x in i]
            print(' '.join(presentation))
        print()

    def rotate(self):
        if self.frozen:
            self.show()
            return None
        self.position = (self.position + 1) % 4
        self.down()

    def right(self):
        if self.frozen:
            self.show()
            return None
        acceptably = True
        for i in self.piece[self.position]:
            if (i + 1) % self.width == 0:
                acceptably = False
        if acceptably:
            for i in range(4):
                for j in range(4):
                    self.piece[i][j] = self.piece[i][j] + 1
        self.down()

    def left(self):
        if self.frozen:
            self.show()
            return None
        acceptably = True
        for i in self.piece[self.position]:
            if i % self.width == 0:
                acceptably = False
        if acceptably:
            for i in range(4):
                for j in range(4):
                    self.piece[i][j] = self.piece[i][j] - 1
        self.down()

    def down(self):
        if self.frozen:
            self.show()
            return None
        for i in self.piece[self.position]:
            if (i + self.width) >= self.width * self.height or self.board[i // self.width + 1][i % self.width] == 1:
                self.frozen = True
                for j in self.piece[self.position]:
                    self.board[j // self.width][j % self.width] = 1
                self.check_game_over()
                self.piece = None
                break
        if not self.frozen:
            for i in range(4):
                for j in range(4):
                    self.piece[i][j] += self.width
        self.show()

    def check_game_over(self):
        for i in range(self.width):
            if all(self.board[j][i] == 1 for j in range(self.height)):
                self.gameOver = True

    def break_rows(self):
        for i in range(self.height - 1, -1, -1):
            while all(j == 1 for j in self.board[i]):
                for k in range(i, 0, -1):
                    self.board[k] = copy.deepcopy(self.board[k - 1])
                for z in range(self.width):
                    self.board[0][z] = 0
        self.show()


O = [[4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6], [4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25], [5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24], [4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
dimension = input().split()
tetris = Tetris(int(dimension[0]), int(dimension[1]))
while True:
    command = input()
    if command.startswith('rotate'):
        tetris.rotate()
    elif command.startswith('right'):
        tetris.right()
    elif command.startswith('left'):
        tetris.left()
    elif command.startswith('down'):
        tetris.down()
    elif command.startswith('piece'):
        symbol = input()
        if symbol == 'O':
            tetris.add_piece(O)
        elif symbol == 'I':
            tetris.add_piece(I)
        elif symbol == 'S':
            tetris.add_piece(S)
        elif symbol == 'Z':
            tetris.add_piece(Z)
        elif symbol == 'L':
            tetris.add_piece(L)
        elif symbol == 'J':
            tetris.add_piece(J)
        elif symbol == 'T':
            tetris.add_piece(T)
    elif command.startswith('exit'):
        break
    elif command.startswith('break'):
        tetris.break_rows()
    if tetris.gameOver:
        print("Game Over!")
        break
