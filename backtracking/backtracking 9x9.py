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
    coloana_vals = 
    
def rezolvare(puzzle):
    # backtracking

    rand, coloana = cauta_urm_camp(puzzle)
    
    if rand is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, rand, coloana)