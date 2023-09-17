import random

def small_board():
    list_random = []
    while len(list_random) < 9:
        number = random.randint(1,9)
        if number not in list_random:
            list_random.append(number)
        else:
            continue
    list_split = [list_random[i:i + 3] for i in range(0, len(list_random), 3)]
    return list_split

def generate_big_board(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            [board[i][j:j + 3], board[i + 1][j:j + 3], board[i + 2][j:j + 3]] = small_board()
    return board


def print_board(board):
    board = generate_big_board(board)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(f"{board[i][j]} ", end="")
        print()

def check_list(list_numbers):
    set_row = set()
    for check_number in list_numbers:
        if check_number in set_row:
            return True
        set_row.add(check_number)
    return False
            
def check_row_sudoku(board):
    error = 0 
    for list_numbers in board:
        repetition = check_list(list_numbers) 
        if repetition == True:
            error += 1
    print_error(error, "wierszach")
            
def check_column_sudoku(board):
    error = 0
    for row in range(0,9):
        checking_list = []
        for column in range(0,9):
            checking_list.append(board[column][row])
        repetition = check_list(checking_list) 
        if repetition == True:
            error += 1
    print_error(error, "kolumnach")
  
def print_error(errors, text):   
    if errors > 0:
        print(f"W {errors} {text} liczby powtarzają się ")
    else:
        print(f"Liczby nie powtarzają się w {text} !")

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

perfect_sudoku = [
    [1,3,7,9,8,6,4,5,2],
    [9,2,5,3,4,7,1,6,8],
    [8,6,4,5,2,1,9,7,3],
    [7,5,3,8,1,4,6,2,9],
    [6,1,2,7,3,9,8,4,5],
    [4,8,9,6,5,2,3,1,7],
    [5,7,1,4,9,3,2,8,6],
    [2,9,8,1,6,5,7,3,4],
    [3,4,6,2,7,8,5,9,1]
]


print_board(board)
check_row_sudoku(board)
check_column_sudoku(board)




