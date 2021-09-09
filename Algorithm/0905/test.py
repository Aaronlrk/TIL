def solution(a, b, g, s, w, t):
    answer = []
    for i in range(len(w)):

        cnt = 0
        if g[i] > 0 and a - w[i] >= 0:
            cnt_1 = 0
            while a >= 0:
                if a-w[i]<=0:
                    break

                cnt_1 += 2
                a -= w[i]
                g[i] -= w[i]

            cnt += cnt_1

        if s[i] > 0 and b - w[i] >= 0:
            cnt_2 = 0
            while b >= 0:
                if b-w[i]<=0:
                    break
                cnt_2 += 2
                b -= w[i]
                s[i] -= w[i]`
            cnt += cnt_2
        answer.append((cnt+1)*t[i])

    return max(answer)


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))

# def solution(a, s):
#     answer = []
#     temp = []
#     check(a[:4], 0)
#     return answer
#
#
# def check(data, cnt):
#     global answer,temp
#     if cnt == len(data):
#         answer.append(temp)
#         return
#     if data[cnt - 1] and data[cnt] == data[cnt - 1]:
#         check(data, cnt + 1)
#         data[cnt] = [data[cnt], data.pop(cnt - 1)]
#         temp.append(cnt)
#         check(data, cnt)
#
#
# print(solution([1, 1, 1, 1, 1, 1, 2, 5, 8, 2, 1, 1, 4, 8, 8, 8, 12, 6, 6], [4, 3, 1, 5, 6]))
