import sys

# bfs를 이용한 문제 한방향으로 벽이나 구멍을 찾을 때까지 움직인다 단 동시에, 최종위치가 겹치는 경우에는 이동거리가 더 많은 것을 한칸 당긴다.
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def move(x, y, dx, dy):
    cnt = 0
    while data[x + dx][y + dy] != '#':
        if data[x + dx][y + dy] == 'O':
            return x + dx, y + dy, cnt
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def BFS(start):
    queu = deque()
    queu.append(start)
    visit = [start]
    while queu:
        xb, yb, xr, yr, answer = queu.popleft()
        if answer > 10:
            break
        for i in range(4):
            nxr, nyr, rcnt = move(xr, yr, dx[i], dy[i])
            nxb, nyb, bcnt = move(xb, yb, dx[i], dy[i])
            if data[nxb][nyb] != 'O':
                if data[nxr][nyr] == 'O':
                    return answer
                if nxr == nxb and nyr == nyb:
                    if rcnt > bcnt:
                        nxr -= dx[i]
                        nyr -= dy[i]
                    else:
                        nxb -= dx[i]
                        nyb -= dy[i]

                if (nxb, nyb, nxr, nyr) not in visit:
                    visit.append((nxb, nyb, nxr, nyr))
                    queu.append((nxb, nyb, nxr, nyr, answer + 1))
    return -1


for test in range(7):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(N):
        for j in range(M):
            if data[i][j] == 'B':
                xb, yb = i, j
            elif data[i][j] == 'R':
                xr, yr = i, j

    position = (xb, yb, xr, yr, 1)

    print(BFS(position))
