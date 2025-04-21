import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        n = len(self.board)
        
        # Check rows
        for row in self.board:
            if all([spot == player for spot in row]):
                return True
        
        # Check columns
        for col in range(n):
            if all([self.board[row][col] == player for row in range(n)]):
                return True
        
        # Check diagonals
        if all([self.board[i][i] == player for i in range(n)]):
            return True
        if all([self.board[i][n - 1 - i] == player for i in range(n)]):
            return True
        
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()
        print()

    def get_empty_spots(self):
        empty_spots = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    empty_spots.append((i, j))
        return empty_spots

    def minimax(self, is_maximizing):
        if self.has_player_won('O'):
            return 1
        if self.has_player_won('X'):
            return -1
        if self.is_board_filled():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for (row, col) in self.get_empty_spots():
                self.board[row][col] = 'O'
                score = self.minimax(False)
                self.board[row][col] = '-'
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for (row, col) in self.get_empty_spots():
                self.board[row][col] = 'X'
                score = self.minimax(True)
                self.board[row][col] = '-'
                best_score = min(score, best_score)
            return best_score

    def bot_move(self):
        best_score = float('-inf')
        best_move = None
        for (row, col) in self.get_empty_spots():
            self.board[row][col] = 'O'
            score = self.minimax(False)
            self.board[row][col] = '-'
            if score > best_score:
                best_score = score
                best_move = (row, col)

        self.fix_spot(best_move[0], best_move[1], 'O')

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            self.show_board()
            if player == 'X':
                try:
                    print(f'Player {player} turn')
                    row, col = list(map(int, input('Enter row & column numbers to fix spot: ').split()))
                    print()

                    if self.board[row - 1][col - 1] != '-':
                        raise ValueError('The spot is already taken. Try another spot.')

                    self.fix_spot(row - 1, col - 1, player)

                except ValueError as err:
                    print(err)
                    continue

            else:
                print(f'Bot {player} turn')
                self.bot_move()

            game_over = self.has_player_won(player)
            if game_over:
                self.show_board()
                print(f'Player {player} wins the game!')
                continue

            game_over = self.is_board_filled()
            if game_over:
                self.show_board()
                print('Match Draw!')
                continue

            player = self.swap_player_turn(player)

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
