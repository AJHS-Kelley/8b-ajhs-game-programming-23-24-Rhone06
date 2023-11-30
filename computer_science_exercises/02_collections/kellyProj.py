def print_board(board):
    for row in board:
        print(row)

def get_move(player):
    move = input('Player {}, enter your move (row, col): '.format(player))
    return tuple(map(int, move.split(',')))

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_tie(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    winner = None
    while not winner and not is_tie(board):
        print_board(board)
        move = get_move(players[current_player])
        if board[move[0]][move[1]] == '-':
            board[move[0]][move[1]] = players[current_player]
            if is_winner(board, players[current_player]):
                winner = players[current_player]
            current_player = (current_player + 1) % 2
        else:
            print('Invalid move. Try again.')
    print_board(board)
    if winner:
        print('Player {} wins!'.format(winner))
    else:
        print('Tie game.')

tic_tac_toe()