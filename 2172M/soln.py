import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n, m, k = map(int, input().split())
    product = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    # Compute shortest distances from city 1 (0-indexed) to all cities using BFS
    dists = [float("inf")] * n
    dists[0] = 0
    q = deque([0])
    while q:
        city = q.popleft()
        for nei in edges[city]:
            if dists[nei] == float("inf"):
                dists[nei] = dists[city] + 1
                q.append(nei)

    # For each product type, find the max shortest distance among cities producing it
    ans = [0] * k
    for i in range(n):
        typ = product[i] - 1  # 0-based index
        ans[typ] = max(ans[typ], dists[i])

    print(*ans)


solve()
