# Tic Tac Toe

import random

player1total = 0
player2total = 0
class TicTacToe:
  def showInstructions(self):
      print('Welcome to Tic Tac Toe! Here you will take turns playing a 2-player match. When it is your turn, you will input a number to put in your respective letter of X or O. Each number stands for a section of the board shown in the figure below:')
      print()
      print(' 7 | 8 | 9')
      print('-----------')
      print('   |   |')
      print(' 4 | 5 | 6')
      print('-----------')
      print('   |   |')
      print(' 1 | 2 | 3')
      print()
  
  def drawBoard(self, board):
      # This function prints out the board that it was passed.

      # "board" is a list of 10 strings representing the board (ignore index 0)
      print('   |   |')
      print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
      print('   |   |')

  def inputPlayerLetter(self):
      # Lets the player type which letter they want to be.
      # Returns a list with the player's letter as the first item, and the computer's letter as the second.
      letter = ''
      while not (letter == 'X' or letter == 'O'):
          print('Does '  + player1name + ' want to be X or O?')
          letter = input().upper()

      # the first element in the tuple is the player's letter, the second is the computer's letter.
      if letter == 'X':
          return ['X', 'O']
      else:
          return ['O', 'X']

  def whoGoesFirst(self):
      # Randomly choose the player who goes first.
      if random.randint(0, 1) == 0:
          return player2name
      else:
          return player1

  def playAgain(self):
      # This function returns True if the player wants to play again, otherwise it returns False.
      print('Do you want to play again? (yes or no)')
      return input().lower().startswith('y')

  def makeMove(self, board, letter, move):
      board[move] = letter

  def isWinner(self, bo, le):
      # Given a board and a player's letter, this function returns True if that player has won.
      # We use bo instead of board and le instead of letter so we don't have to type as much.
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
      (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
      (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
      (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
      (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
      (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
      (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
      (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

  def isSpaceFree(self, board, move):
      # Return true if the passed move is free on the passed board.
      return board[move] == ' '

  def getPlayerMove(self, board):
      # Let the player type in his move.
      move = ' '
      while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
          print('What is ' + turn + 's next move? (1-9)')
          move = input()
      return int(move)

  def isBoardFull(self, board):
      # Return True if every space on the board has been taken. Otherwise return False.
      for i in range(1, 10):
          if self.isSpaceFree(board, i):
              return False
      return True

  def printScoreboard(self, player1score, player2score):
      global player1total
      global player2total
      global player1
      global player2
      player1total += player1score
      player2total += player2score
      print()
      print('Scoreboard:')
      print(player1name + ":" + str(player1total))
      print(player2name + ":" + str(player2total))
game = TicTacToe()
game.showInstructions()
print('What is Player 1\'s name?')
player1name = input()
print('What is Player 2\'s name?')
player2name = input()
while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, player2Letter = game.inputPlayerLetter()
    turn = game.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == player1name:
            # Player 1's turn.
            game.drawBoard(theBoard)
            move = game.getPlayerMove(theBoard)
            game.makeMove(theBoard, playerLetter, move)
            game.drawBoard(theBoard)

            if game.isWinner(theBoard, playerLetter):
                print(player1name + ' won the game!')
                game.printScoreboard(1,0)
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    game.printScoreboard(0,0)
                    break
                else:
                    turn = player2name

        else:
            # Player 2's turn.
            move = game.getPlayerMove(theBoard)
            game.makeMove(theBoard, player2Letter, move)

            if game.isWinner(theBoard, player2Letter):
                print(player2name + ' won the game!')
                game.printScoreboard(0,1)
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    game.printScoreboard(0,0)
                    break
                else:
                    turn = player1name

    if not game.playAgain():
        break

