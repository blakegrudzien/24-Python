import copy
import random
from threading import main_thread
import array





print("world")

def main():
  board = init_board()
  print_board(board)
  sol = get_solutions(board)
  print_solutions(sol)
  
  

  


def init_board():
  board = []
  for i in range(4):
    board.append(random.randint(1, 9)) 
  return board


def print_board(board):
  print(board[0],board[1], board[2], board[3])
  
def print_solutions(solutions):
  if len(solutions) == 0:
    print("No Solutions")
  for x in solutions:
    print(x)
  
      

def get_solutions(num):
    
  
  current = []
  solutions = []
  
  helper(solutions,num, current, -1, -1, -1)
  
  return solutions
     

    
def helper(solutions, num, current, p1, p2, op): 
  if p1 != -1:
    spot = min(p1,p2)
    current.append(str(num[p1]))
    not_spot = max(p1,p2)
    

    if op == 0:
      
      current.append('+')
      current.append(str(num[p2]))
      num[spot] = num[p1] + num[p2]
      num[not_spot] = 0
    elif op == 1:
      
      current.append('-')
      current.append(str(num[p2]))
      num[spot] = num[p1] - num[p2]
      num[not_spot] = 0
    elif op == 2:
      
      current.append('*')
      current.append(str(num[p2]))
      num[spot] = num[p1] * num[p2]
      num[not_spot] = 0
    elif op == 3:
        
        current.append('/')
        current.append(str(num[p2]))
        num[spot] = num[p1] / num[p2]
        num[not_spot] = 0
    current.append('=')
    current.append(num[spot])
    current.append('|')
    current.append('|')
    
    if len(current) >= 21:
      if num[spot]==24:
        current.pop()
        current.pop()
        solutions.append(current.copy())
      return

    
  for i in range(4):
    if num[i] != 0:
      for j in range(4):
        if num[j] !=0 and i !=j and num[i]>=num[j]:
          if num[i] != num[j]:
            helper(solutions,num.copy(), current.copy(), i, j, 0) # +
            helper(solutions,num.copy(), current.copy(),  i, j, 2) #*
          helper(solutions,num.copy(), current.copy(),  i, j, 1) #-
          if num[i] % num[j] == 0:
            helper(solutions,num.copy(), current.copy(),  i, j, 3)# /

  

main()


          
             


       