from random import randint as rand

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(w, h):
    tw = rand(0, w)
    th = rand(0, h)
    return(th, tw)

#0 - up, 1 -right, 2 - down, 3 - left
def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 4)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)
