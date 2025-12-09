import sys

input = sys.stdin.readline


def solve():
    x, y, z = map(int, input().split())
    if max(x, y, z) - min(x, y, z) >= 10:
        print("check again")
    else:
        print("final", sorted([x, y, z])[1])


solve()
