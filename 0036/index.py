def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
ans = 0
for i in range(n + 1, 2 * n):
    if is_prime(i):
        ans += 1
print(ans)