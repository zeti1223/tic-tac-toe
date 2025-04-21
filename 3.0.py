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

    def easy_bot_move(self):
        # Try to win
        for (row, col) in self.get_empty_spots():
            self.board[row][col] = 'O'
            if self.has_player_won('O'):
                return
            self.board[row][col] = '-'

        # Block X from winning
        for (row, col) in self.get_empty_spots():
            self.board[row][col] = 'X'
            if self.has_player_won('X'):
                self.board[row][col] = 'O'
                return
            self.board[row][col] = '-'

        # If no immediate win or block, choose a random empty spot
        row, col = random.choice(self.get_empty_spots())
        self.board[row][col] = 'O'

    def minimax(self, depth, is_maximizing):
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
                score = self.minimax(depth + 1, False)
                self.board[row][col] = '-'
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for (row, col) in self.get_empty_spots():
                self.board[row][col] = 'X'
                score = self.minimax(depth + 1, True)
                self.board[row][col] = '-'
                best_score = min(score, best_score)
            return best_score

    def hard_bot_move(self):
        best_score = float('-inf')
        best_move = None
        for (row, col) in self.get_empty_spots():
            self.board[row][col] = 'O'
            score = self.minimax(0, False)
            self.board[row][col] = '-'
            if score > best_score:
                best_score = score
                best_move = (row, col)

        self.fix_spot(best_move[0], best_move[1], 'O')

    def start(self):
        self.create_board()

        print("Choose game mode:")
        print("1. Player vs Player")
        print("2. Player vs Easy Bot")
        print("3. Player vs Hard Bot")

        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
            self.player_vs_player()
        elif choice == 2:
            self.player_vs_easy_bot()
        elif choice == 3:
            self.player_vs_hard_bot()
        else:
            print("Invalid choice! Please restart the game and choose a valid option.")

    def player_vs_player(self):
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            self.show_board()
            print(f'Player {player} turn')
            try:
                row, col = list(map(int, input('Enter row & column numbers to fix spot: ').split()))
                print()

                if self.board[row - 1][col - 1] != '-':
                    raise ValueError('The spot is already taken. Try another spot.')

                self.fix_spot(row - 1, col - 1, player)

            except ValueError as err:
                print(err)
                continue

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

    def player_vs_easy_bot(self):
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            self.show_board()
            if player == 'X':
                print(f'Player {player} turn')
                try:
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
                self.easy_bot_move()

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

    def player_vs_hard_bot(self):
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            self.show_board()
            if player == 'X':
                print(f'Player {player} turn')
                try:
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
                self.hard_bot_move()

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
