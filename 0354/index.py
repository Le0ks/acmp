# не обязательно проходить циклом до тех пор, пока число станет n == 1
# можно пройтись до sqrt(n) если в n что-то ещё осталось > 1 то, это и есть само число n
# значит в данном случаи ответ n

n = int(input())
d = 2
while d * d <= n:
    if n % d == 0:
        n //= d
        print(d, end="")
        if n > 1:
            print("*", end="")
    else:
        d += 1
if n > 1:
    print(n)