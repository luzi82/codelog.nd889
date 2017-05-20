from utils import *
import copy

def eliminate(values):
    # Write a function that will take as an input, the sudoku in dictionary form,
    # run through all the boxes, applying the eliminate technique,
    # and return the resulting sudoku in dictionary form.
    ret = copy.copy(values)
    for pk, pv in peers.items():
        if len(values[pk]) != 1:
            continue
        for p in pv:
            ret[p] = ret[p].replace(values[pk],'')
    return ret
