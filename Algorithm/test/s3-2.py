import math


def solution(fees, records):
    answer = []
    check = []
    result = {i.split()[1]:0 for i in records}
    for i in range(len(records)-1):
        total = 0
        for j in range(i+1,len(records)):
            if records[i].split()[1] == records[j].split()[1] and records[i].split()[2] == 'IN':
                mf, ml = int(records[i].split()[0][3:]), int(records[j].split()[0][3:])
                hf, hl = int(records[i].split()[0][:2]), int(records[j].split()[0][:2])
                h, m = 0, 0
                if mf > ml:
                    hl -= 1
                    ml += 60
                    h = hl - hf
                    m = ml - mf
                    total = (h * 60) + m

                else:
                    h = hl - hf
                    m = ml - mf
                    total = (h * 60) + m
                result[records[i].split()[1]]+=total
                check.append(records[i])
                check.append(records[j])
                break
    for i in records:
        if i not in check:
            mf, ml = int(i.split()[0][3:]), 59
            hf, hl = int(i.split()[0][:2]), 23
            h, m = 0, 0
            if mf > ml:
                hl -= 1
                ml += 60
                h = hl - hf
                m = ml - mf
                total = (h * 60) + m

            else:
                h = hl - hf
                m = ml - mf
                total = (h * 60) + m
            result[i.split()[1]] += total


    final = []
    for i in result:
        fee = 0

        if result[i] < fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + (math.ceil((result[i] - fees[0]) / fees[2])) * fees[3]
        final.append((i, fee))
    final.sort()
    for i in final:
        answer.append(i[1])

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
