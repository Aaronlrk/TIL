T= int(input())

for i in range(T):
    numbers = list(map(int,input().split()))
    msum = numbers[0]
    for j in numbers:
        if msum<j:
            msum,j=j,msum
    print(f'#{i+1} {msum}')