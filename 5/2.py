import sys
import re
input = sys.stdin.read().strip().split("\n\n")

seeds = list(map(int, re.match("seeds:(.*)$", input[0]).groups()[0].strip().split()))

ranges = []
for idx in range(0, len(seeds), 2):
    ranges.append((seeds[idx], seeds[idx+1]))
ans = []

for s in ranges:
    current_seed = s[0]
    while current_seed != s[0]+s[1]:
        skip = [(s[0]+s[1])-current_seed]
        loc = current_seed
        for l in map(lambda x: x.split("\n"), input[1:]):
            for mapping in l[1:]:
                a, b, c = map(int, mapping.split())
                if b <= loc and loc < b+c:
                    skip.append(c-(loc-b))
                    loc = a+(loc-b)
                    break
                if b > loc:
                    skip.append(b-loc)
        ans.append(loc)
        current_seed += min(skip)
print(min(ans))
