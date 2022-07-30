
n = list(map(int, input().split()))
a = n.index(0)
n = n[:a]
n.sort()
print(n[-2])