import sys
import re
input = sys.stdin.read().strip().split()
ans = 0
mp = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9")
]
for i in range(1, 9+1):
    mp.append((str(i), str(i)))
for line in input:
    left_idx = 1000
    right_idx = -1000
    left = 0
    right = 0
    for a,b in mp:
        idx = line.find(a)
        if idx != -1 and idx < left_idx:
            left_idx = idx
            left = b
        idx = line.rfind(a)
        if idx != -1 and idx > right_idx:
            right_idx = idx
            right = b
    
    for c in range(ord('a'), ord('z')+1):
        line = line.replace(chr(c), "")
    ans += int(left+right)
print(ans)
