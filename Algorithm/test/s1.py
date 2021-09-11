def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    result = [0 for _ in range(len(id_list))]
    temp = {}
    for i in id_list:
        temp[i]=[]
    for j in range(len(report)):
        temp[report[j].split()[0]].append(report[j].split()[1])
    for h in temp:
        temp[h] = set(temp[h])
    for q in temp:
        for x in temp[q]:
            result[id_list.index(x)]+=1
    for y in range(len(result)):
        if result[y]>=int(k):

            for z in temp:
                if id_list[y] in temp[z]:
                    answer[id_list.index(z)]+=1



    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))