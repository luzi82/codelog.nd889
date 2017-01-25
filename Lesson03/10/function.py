from utils import *
import copy

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    x = reduce_puzzle(values)
    if x == False:
        return False

    # Chose one of the unfilled square s with the fewest possibilities
    min_box = None
    min_len = 999
    for	k,v in values.items():
        if len(v) <= 1:
            continue
        if len(v) >= min_len:
            continue
        min_box = k
        min_len = len(v)

    if min_box == None:
        return values

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for	c in list(values[min_box]):
        values0 = copy.copy(values)
        values0[min_box] = c
        x = search(values0)
        if x !=	False:
            values.update(x)
            return values

    # If you're stuck, see the solution.py tab!
    return False

