import itertools
from time import time

def stone_combo(n):
    a = itertools.product([0,1,3,4], repeat=n)
    a2 = [i for i in a if sum(i) == n]
    a3 = []
    for i in a2:
        x = [k for k in i if k!= 0]
        if x not in a3:
            a3.append(x)
                
    return a3