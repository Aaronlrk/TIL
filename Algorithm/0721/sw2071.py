T= int(input())

for i in range(T):
    numbers = list(map(int,input().split()))
    avg = (sum(numbers)/10)
    if avg % 1 >= 0.5:
        print(f'#{i+1} {int(avg)+1}')
    else:
        print(f'#{i+1} {int(avg)}')
    # mysum =0
    # for j in numbers:
    #     if j&1:
    #         mysum+= j
    # avg = mysum/10       
    # print(f'#{i+1} {avg}')
