def solution(board, skill):
    answer = 0
    for i in skill:
        x1, y1 = i[1], i[2]
        x2, y2 = i[3], i[4]
        damage = i[5]
        if i[0] == 1:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    board[x][y] -= damage

        if i[0] == 2:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    board[x][y] += damage

    for i in board:
        for j in i:
            if j > 0:
                answer += 1
    print(map(-4,[5,5,5,5,5]))
    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
