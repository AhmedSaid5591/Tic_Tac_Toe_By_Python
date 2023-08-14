import random
def create_board():
  board = []
  for row in range(3):
    board.append([" "] * 3)
  return board


def print_board(board):
  for row in board:
    for square in row:
      print(square, end=" ")
    print()

def handle_player_move(board, player_symbol):
  while True:
    print(f"Player {player_symbol}, please enter your move (1-9):")
    move = input()
    move = int(move) - 1
    if 0 <= move <= 8 and board[move // 3][move % 3] == " ":
      board[move // 3][move % 3] = player_symbol
      break

def check_for_win(board, player_symbol):
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2] == player_symbol:
      return True
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] == player_symbol:
      return True
  if board[0][0] == board[1][1] == board[2][2] == player_symbol:
    return True
  if board[0][2] == board[1][1] == board[2][0] == player_symbol:
    return True
  return False

def check_for_tie(board):
  for row in board:
    if " " in row:
      return False
  return True

def main():
  board = create_board()
  player_symbols = ["X", "O"]
  current_player = random.choice(player_symbols)
  while not check_for_win(board, current_player) and not check_for_tie(board):
    print_board(board)
    handle_player_move(board, current_player)
    current_player = player_symbols[player_symbols.index(current_player) ^ 1]

  if check_for_win(board, current_player):
    print(f"Player {current_player} wins!")
  elif check_for_tie(board):
    print("The game is a tie!")


main()