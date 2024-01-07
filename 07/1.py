import sys
import collections
import functools
input = list(map(lambda x: x.split(), sys.stdin.read().strip().split("\n")))


order = {}

for idx,x in enumerate(["A", "K", "Q", "J", "T", "9", "8","7","6","5","4","3","2"]):
    order[x] = -idx


def rank(hand):
    cards = collections.defaultdict(int)
    for card in hand:
        cards[card] += 1
    if 5 in cards.values():
        return 7
    if 4 in cards.values():
        return 6
    if 3 in cards.values() and 2 in cards.values():
        return 5
    if 3 in cards.values() and len(cards) == 3:
        return 4
    if len(list(filter(lambda x: x==2, cards.values()))) == 2:
        return 3
    if 2 in cards.values() and len(cards) == 4:
        return 2
    if len(cards) == 5:
        return 1
    assert False

def cmp(A, B):
    a = A[0]
    b = B[0]
    if rank(a) < rank(b):
        return -1
    if rank(a) > rank(b):
        return 1
    for x in range(5):
        if order[a[x]] < order[b[x]]:
            return -1
        elif order[a[x]] > order[b[x]]:
            return 1
    assert False

input = sorted(input, key=functools.cmp_to_key(cmp))
ans = 0
for idx,x in enumerate(input):
    ans += (idx+1)*int(x[1])
print(ans)
