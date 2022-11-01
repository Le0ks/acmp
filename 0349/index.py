m, n = map(int, input().split())
l = [True for i in range(n)]
flag = True
for i in range(1, n):
    if l[i]:
        for j in range(2 * i + 1, n, i  + 1):
            l[j] = False
        if i + 1 >= m:
            flag = False
            print(i + 1)
if flag:
    print("Absent")