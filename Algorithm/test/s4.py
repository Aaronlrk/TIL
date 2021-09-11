from itertools import combinations


def solution(n, info):
    temp = [[info[i] + 1, abs(i - 10)] for i in range(len(info))]
    a = [[info[i], abs(i - 10)] for i in range(len(info))]

    a_total = 0
    a_score = []
    for i in a:
        if i[0]:
            a_score.append(i[1])
    for i in a:
        if i[0]:
            a_total += i[1]
    result = []
    for i in range(len(temp)):
        for j in list(combinations(temp, i)):
            tsum = 0

            for h in j:
                tsum += h[0]
            if tsum == n:
                result.append(j)
    sum_result = []
    my_max = 0
    for i in result:
        tsum2 = 0
        a_temp = a_total
        for j in i:
            tsum2 += j[1]
            if j[1] in a_score:
                a_temp -= j[1]

        if my_max < tsum2 - a_temp:
            my_max = tsum2 - a_temp

            sum_result.append(i)

    answer = [0 for _ in range(11)]

    for i in sum_result[-1]:
        answer[abs(i[1] - 10)] = i[0]
    # print(answer)
    # print(my_max)
    if answer != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        return answer
    else:

        return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
