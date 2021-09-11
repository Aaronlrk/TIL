def DFS(info, graph, start, visit=[], wolf=0, sheep=0):

    visit.append(start)

    temp = graph[start]
    for node in graph[start]:
        if node not in visit:
            if info[node] == 0:
                sheep+=1
                DFS(info, graph, node, visit,wolf,sheep)
            if info[node] == 1 :
                wolf+=1
                DFS(info, graph, node, visit,wolf,sheep)
                wolf -= 1

    print(sheep)
    return visit


def solution(info, edges):
    answer = 0
    graph = {x: [] for x in range(len(info))}

    for i in edges:
        graph[i[0]].append(i[1])


    # if info[start] == 0:
    # elif info[start] ==1:
    print(DFS(info, graph, 0, [],0,1))
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
