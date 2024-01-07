import sys
import heapq
input = sys.stdin.read().split()


def oob(y,x):
    if min(x,y) < 0 or x >= len(input[0]) or y >= len(input):
        return True
    return False

vis = set()
ans = 10000000000
q = []
heapq.heappush(q, (-int(input[0][0]), ((0, 0), "right", 0)))
while len(q) > 0:
    cost,state = heapq.heappop(q)
    if state in vis or oob(*state[0]) or state[2] > 10:
        continue
    cost += int(input[state[0][0]][state[0][1]])
    vis.add(state)
    if state[0][0] == len(input)-1 and state[0][1] == len(input[0])-1 and state[2] >= 4:
        ans = min(ans, cost)
    if state[1] == 'right':
        heapq.heappush(q, (cost, ((state[0][0], state[0][1]+1), "right", state[2]+1)))
        if state[2] < 4:
            continue
        heapq.heappush(q, (cost, ((state[0][0]-1, state[0][1]), "up", 1)))
        heapq.heappush(q, (cost, ((state[0][0]+1, state[0][1]), "down", 1)))
    elif state[1] == 'left':
        heapq.heappush(q, (cost, ((state[0][0], state[0][1]-1), "left", state[2]+1)))
        if state[2] < 4:
            continue
        heapq.heappush(q, (cost, ((state[0][0]-1, state[0][1]), "up", 1)))
        heapq.heappush(q, (cost, ((state[0][0]+1, state[0][1]), "down", 1)))
    elif state[1] == 'up':
        heapq.heappush(q, (cost, ((state[0][0]-1, state[0][1]), "up", state[2]+1)))
        if state[2] < 4:
            continue
        heapq.heappush(q, (cost, ((state[0][0], state[0][1]-1), "left", 1)))
        heapq.heappush(q, (cost, ((state[0][0], state[0][1]+1), "right", 1)))
    elif state[1] == 'down':
        heapq.heappush(q, (cost, ((state[0][0]+1, state[0][1]), "down", state[2]+1)))
        if state[2] < 4:
            continue
        heapq.heappush(q, (cost, ((state[0][0], state[0][1]-1), "left", 1)))
        heapq.heappush(q, (cost, ((state[0][0], state[0][1]+1), "right", 1)))

print(ans)
