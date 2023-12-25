import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.read().strip().split()

vis = set()
def haku(s):
    if s in vis:
        return
    loc = s[0]
    ofs = s[1]
    if min(loc) < 0 or loc[0] >= len(input) or loc[1] >= len(input[0]):
        return
    vis.add(s)
    if input[loc[0]][loc[1]] == '.':
        haku(((loc[0]+ofs[0], loc[1]+ofs[1]), (ofs[0], ofs[1])))
    elif input[loc[0]][loc[1]] == '|':
        if ofs[1] != 0:
            haku(((loc[0], loc[1]), (1,0)))
            haku(((loc[0], loc[1]), (-1,0)))
        else:
            haku(((loc[0]+ofs[0], loc[1]+ofs[1]), (ofs[0], ofs[1])))

    elif input[loc[0]][loc[1]] == '-':
        if ofs[0] != 0:
            haku(((loc[0], loc[1]), (0,1)))
            haku(((loc[0], loc[1]), (0,-1)))
        else:
            haku(((loc[0]+ofs[0], loc[1]+ofs[1]), (ofs[0], ofs[1])))
    elif input[loc[0]][loc[1]] == '/':
        if ofs[0] == 1:
            haku(((loc[0], loc[1]-1), (0,-1)))
        elif ofs[0] == -1:
            haku(((loc[0], loc[1]+1), (0,+1)))
        elif ofs[1] == 1:
            haku(((loc[0]-1, loc[1]), (-1,0)))
        elif ofs[1] == -1:
            haku(((loc[0]+1, loc[1]), (+1,0)))
    elif input[loc[0]][loc[1]] == '\\':
        if ofs[0] == 1:
            haku(((loc[0], loc[1]+1), (0,+1)))
        elif ofs[0] == -1:
            haku(((loc[0], loc[1]-1), (0,-1)))
        elif ofs[1] == 1:
            haku(((loc[0]+1, loc[1]), (+1,0)))
        elif ofs[1] == -1:
            haku(((loc[0]-1, loc[1]), (-1,0)))
    else:
        assert False

haku(((0,0), (0,1)))

st = set(map(lambda x: x[0], vis))
print(len(st))
