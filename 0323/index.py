def is_prime(n):
    for _ in range(2, int(n ** 0.5) + 1):
        if n % _ == 0:
            return False
    return True

n = int(input())
for i in range(2, n // 2 + 1): # перебираем до половины т.к. после половины числа будут повторяться только в обратном порядке
    if is_prime(i) and is_prime(n - i):
        print(i, n - i)
        break
