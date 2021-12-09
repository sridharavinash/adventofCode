import numpy as np
import re

def process_input_file(filename):
  regex = r"(\w+)"
  boards = []
  with open(filename, 'r') as f:
    lines = f.readlines()
    draws = [int(x) for x in lines[0].strip().split(',')]
    b = []
    for line in lines[2:]:
      if line.strip() == '':
        board = np.array(b)
        boards.append(board)
        b = []
        continue
      else:
        matches = re.findall(regex, line)
        b.append([int(x) for x in matches])
  return boards, draws

def part1(input):
  boards, draws = input
  winning_board = []
  winning_num = draws[0]
  s = 0
  for curr in draws:
    if len(winning_board) != 0:
      break
    print("draw:", curr)
    for board in boards:
      board[board == curr] = -1
      row_bingo = (board == -1).all(axis = 1)
      col_bingo = (board == -1).all(axis = 0)
      #print(board)
      #print(row_bingo, col_bingo)
      if row_bingo.any() or col_bingo.any():
        winning_board = board
        sboard = np.where(board != -1, board, 0)
        s = np.sum(sboard)
        winning_num = curr
        break
      #print()
  print(winning_board,s, winning_num)
  print(winning_num * s)
      

def part2(input):
  boards, draws = input
  winning_board = []
  winning_num = draws[0]
  s = 0
  for curr in draws:
    print("draw:", curr)
    i = 0
    if len(boards) == 0:
      break
    while i <= len(boards)-1:
      board = boards[i]
      board[board == curr] = -1
      row_bingo = (board == -1).all(axis = 1)
      col_bingo = (board == -1).all(axis = 0)
      #print(board)
      #print(row_bingo, col_bingo)
      if row_bingo.any() or col_bingo.any():
        winning_board = board
        sboard = np.where(board != -1, board, 0)
        s = np.sum(sboard)
        winning_num = curr
        boards.pop(i)
        print(winning_board,s, winning_num)
        continue
      i+=1
  print(winning_board,s, winning_num)
  print(winning_num * s)

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #part1(inp)
  part2(inp)
