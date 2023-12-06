import sys
import re
input = sys.stdin.read().strip().split("\n\n")

seeds = list(map(int, re.match("seeds:(.*)$", input[0]).groups()[0].strip().split()))

for l in map(lambda x: x.split("\n"), input[1:]):
    g = re.match("(.*?)-to-(.*?) map:", l[0]).groups()
    for idx, s in enumerate(seeds):
        for mapping in l[1:]:
            a, b, c = map(int, mapping.split())
            if b <= s and s < b+c:
                seeds[idx] = a+(s-b)
                break
print(min(seeds))
