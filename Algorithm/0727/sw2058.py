N = int(input())

msum = 0
while N>1:
    msum += N%10
    N //= 10
print(msum)
