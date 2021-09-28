import sys

sys.stdin = open('input_17471.txt')


def bfs(sector, N):
    q = [sector[0]]
    visited = [0] * (N + 1)
    visited[sector[0]] = 1
    total = 0
    while q:
        node = q.pop(0)
        total += people[node]
        for i in sector:
            if tree[node][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[node] + 1

    for i in sector:
        if visited[i] == 0:
            return 0
    return total


N = int(input())

people = [0] + list(map(int, input().split()))

tree = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in temp[1:]:
        tree[i][j] = 1
        tree[j][i] = 1

answer = 1e9

for i in range(1, (1 << N) // 2):
    first = []
    second = []
    for j in range(N):
        if i & (1 << j) != 0:
            first.append(j + 1)
        else:
            second.append(j + 1)

    total_f = bfs(first, N)
    total_s = bfs(second, N)
    if total_f * total_s:
        if answer > abs(total_f - total_s):
            answer = abs(total_f - total_s)

if answer == 1e9:
    answer = -1

print(answer)
