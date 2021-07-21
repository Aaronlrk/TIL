def all_list_sum(lst):
    sum = 0
    for i in range(len(lst)):
        for j in range(i+1):
            sum += lst[i][j]
    print(sum)



all_list_sum([[1], [2,3], [4,5,6], [7,8,9,10]])