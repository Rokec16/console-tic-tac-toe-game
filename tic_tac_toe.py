class TicTacToe():

    def __init__(self):
        self.game_over = False
        self.game_won = False
        self.symbols = ['X', 'O']
        self.player = 0
        self.board = [' ' for _ in range(10)]

    def __str__(self):
        return 'Welcome to Console Tic Tac Toe!'

    def reset_board(self):
        '''Create an empty playing board.'''
        self.board = [' ' for _ in range(10)]

    def display_board(self):
        '''Displays the playing board to players.'''

        print('-------')
        print(f'|{self.board[6]}|{self.board[7]}|{self.board[8]}|')
        print('-------')
        print(f'|{self.board[3]}|{self.board[4]}|{self.board[5]}|')
        print('-------')
        print(f'|{self.board[0]}|{self.board[1]}|{self.board[2]}|')
        print('-------')

    def update_board(self):
        '''Asks the user to select a location on the board and places
        a symbol on the selected location if this is possible.'''

        input_valid = False
        while not input_valid:
            user_input = input('Enter position [1 - 9]: ')
            if user_input.isnumeric():
                position = int(user_input)
                if 1 <= position <= 9:
                    input_valid = True
                    if self.board[position - 1] == ' ':
                        self.board[position - 1] = self.symbols[self.player]
                    else:
                        print('This field is already taken.')
                else:
                    print('Please enter a valid number.')
            else:
                print('Please enter a valid number.')

    def check_win_conditions(self):
        '''Checks if the game has been won.'''

        return \
            self.symbols[self.player] == self.board[0] == self.board[1] == self.board[2] or \
            self.symbols[self.player] == self.board[3] == self.board[4] == self.board[5] or \
            self.symbols[self.player] == self.board[6] == self.board[7] == self.board[8] or \
            self.symbols[self.player] == self.board[0] == self.board[3] == self.board[6] or \
            self.symbols[self.player] == self.board[1] == self.board[4] == self.board[7] or \
            self.symbols[self.player] == self.board[2] == self.board[5] == self.board[8] or \
            self.symbols[self.player] == self.board[0] == self.board[4] == self.board[8] or \
            self.symbols[self.player] == self.board[2] == self.board[4] == self.board[6]

    def switch_player(self):
        self.player = 1 if self.player == 0 else 0

    def replay(self):
        '''Ask players if they want to repeat the game.'''
        input_valid = False
        while not input_valid:
            user_input = input('Do you want to play again? Enter Yes or No: ')
            if user_input == 'Yes' or user_input == 'No':
                input_valid = True
                return True if user_input == 'Yes' else False
            else:
                print('Please enter Yes or No.')


def main():
    game = TicTacToe()

    print(game)

    while not game.game_over:

        game.update_board()
        game.display_board()
        game.game_won = game.check_win_conditions()

        if game.game_won:
            print(f'Player {game.player} wins the game!')
            game.game_over = not game.replay()
            if game.game_over:
                print('Thank you for playing. Goodbye.')
            else:
                game.reset_board()
                game.player = 0
        else:
            game.switch_player()


if __name__ == '__main__':
    main()
