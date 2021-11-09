def solution(scores):
    answer = ''
    scores = list(map(list,zip(*scores)))
    avgs = []

    for idx, val in enumerate(scores):
        avg = sum(val)
        n = len(val)

        if val[idx]==max(val) or val[idx]==min(val):
            if val.count(val[idx]) ==1:
                avg -=val[idx]
                n-=1
        avgs.append(avg/n)

    for avg in avgs:
        if avg >= 90:
            answer += 'A'
        elif 80 <= avg < 90:
            answer += 'B'
        elif 70 <= avg < 80:
            answer += 'C'
        elif 50 <= avg < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer

    # scores = zip(*scores[:])
    # scores = [list(i) for i in scores]
    #
    #
    # for i in range(len(scores)):
    #     for j in range(len(scores[i])):
    #         if i == j:
    #             if scores[i][j] == max(scores[i]) and scores[i].count(max(scores[i])) == 1 :
    #                 scores[i][j] = 0
    #
    #             if  scores[i][j] == min(scores[i]) and scores[i].count(min(scores[i])) == 1:
    #                 scores[i][j] = 0
    #
    # for i in scores:
    #     N = len(i)-i.count(0)
    #     if sum(i):
    #         avg = sum(i) / N
    #     if avg >= 90:
    #         answer += 'A'
    #     elif 80 <= avg < 90:
    #         answer += 'B'
    #     elif 70 <= avg < 80:
    #         answer += 'C'
    #     elif 50 <= avg < 70:
    #         answer += 'D'
    #     else:
    #         answer += 'F'



# solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)],
#                                           map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1],
#                                               ((s[i], s[:i] + s[i + 1:]) for i, s in enumerate(zip(*scores))))))
print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
