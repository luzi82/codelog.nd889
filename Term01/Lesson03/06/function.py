# warning: I believe my code is better than solution.py
# but the web just reject my solution

from utils import *
import copy

def only_choice(values):
    # Write a function that will take as an input, the sudoku in dictionary form,
    # run through all the units, applying the only choice technique,
    # and return the resulting sudoku in dictionary form.
    ret = copy.copy(values)
    loop = True
    while(loop):
        loop = _only_choice(ret)
    #_only_choice(ret)
    return ret

def _only_choice(values):
    ret = False
    for unit in unitlist:
        unit_value = ''.join([values[b] for b in unit])
        for c in list('123456789'):
            if unit_value.count(c) != 1:
                continue
            for box in unit:
                if c not in values[box]:
                    continue
                if values[box] == c:
                    continue
                values[box] = c
                ret = True
    return ret
