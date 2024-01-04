import copy
import random
from threading import main_thread
import array







def main():
  answer = input("Would you like to Play?(y/n)")
  if answer != 'y':
    return
  
  else:
    
    board = init_board()
    sol = get_solutions(board)
    while len(sol)==0:

      board = init_board()
      
      sol = get_solutions(board)
    print("These are your 4 numbers, there is a solution")
    
    temp = board.copy()
  
    while temp[0]!=24 or temp[1] != 0 or temp[2] != 0 or temp[3] != 0 :
      print_board(temp)
      
      response = input("r = restart, s = see solutions, otherwise, enter the the index for the first number (0,1,2,or 3) in the operation then the number corresponding to the operation then the index of the final number")
      
      if response == 'r':
        temp = board.copy()
        print(board)
      if response == 's':
        
        print_solutions(sol)
        print("Better Luck Next Time")
        return
      elif response == '0' or response == '1' or response == '2' or response == '3':
        print(temp[int(response)])
        op_in = input("0 = '+', 1 = '-', 2 = '*', 3 = '/'" )

        while op_in != '0' and op_in != '1' and op_in != '2' and op_in != '3':
          print("enter a valid option")
          op_in = input("0 = '+', 1 = '-', 2 = '*', 3 = '/'" )
        print(temp)
        n2 = input("next number")
        while n2 != '0' and n2 != '1' and n2 != '2' and n2 != '3' and n2 != 'r' and n2 != response:
          print("enter a valid option")
          n2 = input(temp)
        first = min(int(response), int(n2))
        second = max(int(response), int(n2))
        higher = max(temp[first], temp[second])
        lower = min(temp[first], temp[second])

        if op_in == '0':
          temp[first] = higher + lower
          temp[second] = 0
        elif op_in == '1':
          temp[first] = higher - lower
          temp[second] = 0
        elif op_in == '2':
          temp[first] = higher * lower
          temp[second] = 0
        else:
          temp[first] = higher / lower
          temp[second] = 0
    print("Good Job!")



  






  
  
  

  


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


          
             


        