def check(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    x = round(n ** 0.5) + 1
    for i in range(3, x, 2):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    change = ''
    while n > 0:
        n, mod = divmod(n, k)
        change += str(mod)
    temp = change[::-1]

    result = str(temp).split('0')
    for i in result:
        if i != '':
            if check(int(i)):
                answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
