def isPrime(n):
    if n > 0:
        if n % 2 == 0:
            return 0
        else:
            d = 3
            while d * d <= n and n % d != 0:
                d += 2
            if d * d > n:
                return n
    else:
        
a, b, c = map(int, input().split())
sum = 0
if isPrime(a):
    sum += a
if isPrime(b):
    sum += b
if isPrime(c):
    sum += c
if isPrime(sum):
    print(sum)
    print("Yes")
else:
    print(sum)
    print("No")