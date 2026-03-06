from itertools import groupby


s = input().strip()

groups = []
for k, g in groupby(s):

    count = len(list(g))

    groups.append(f"({count}, {k})")

print(" ".join(groups))
