from pprint import pprint

def cautare(puzzle):

    for r in range(9):
        for c in range(9): # range(9) este 0, 1, 2, 3,... 8
            if puzzle[r][c] == -1:
                return r, c    

    return None, None #  daca nu exista -1

def is_valid(puzzle, guess, rand, coloana):

    rand_vals = puzzle[rand]
    if guess is rand_vals:
        return False

    #coloana_vals = []
    #for i in range(9):
     #   coloana_vals.append(puzzle[i][col])
    coloana_vals = [puzzle[i][coloana] for i in range(9)]
    if guess in coloana_vals:
        return False

    rand_start = (rand // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
    coloana_start = (coloana // 3) * 3

    for r in range(rand_start, rand_start + 3):
        for c in range(coloana_start, coloana_start + 3):
            if puzzle[r][c] == guess:
                return False

def rezolvare(puzzle):
    # backtracking

    rand, coloana = cautare(puzzle)
    
    if rand is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, rand, coloana):
            puzzle[rand][coloana] = guess
            if rezolvare(puzzle):
                return True
        puzzle[rand][coloana] = -1 # resetare valoare
    return False  

if __name__ == '__main__':
    exemplu_board = [
        [3, 9, -1,     -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,    7, 1, 9,    -1, 8, -1],

        [-1, 5, -1,    -1, 6, 8,    -1, -1, -1],
        [2, -1, 6,     -1, -1, 3,   -1, -1, 4],
        [-1, -1, -1,   -1, -1, -1,  -1, -1, 4],
    
        [5, -1, -1,    -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,      1, -1, 5,   -1, 4, -1],
        [1, -1, 9,     -1, -1, -1,   2, -1, -1],
    ]
    print(rezolvare(exemplu_board))
    pprint(exemplu_board)