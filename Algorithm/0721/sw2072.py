T= int(input())

for i in range(T):
    numbers = map(int, input().split())
    mysum =0
    for j in numbers:
        if j&1:
            mysum+=j
    print(f'#{i+1} {mysum}')
