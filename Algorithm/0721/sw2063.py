N= int(input())
number = list(map(int, input().split()))

mid = len(number)//2

for i in range(len(number)-1,0,-1):
  for j in range(i):
    if number[j]>number[j+1]:
      number[j],number[j+1] = number[j+1],number[j]
if len(number)%2:
    print(number[mid])
else:
    print(f'{number[mid-1]}{number[mid]}')
# for i in range(len(numbers)-1,0,-1):
#     for j in range(i):
#         if numbers[j] > numbers[j-1]:
#             numbers[j],numbers[j-1]=numbers[j-1],numbers[j]