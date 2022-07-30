n = int(input())
a = list(map(int, input().split()))
l, r = map(int, input().split())
print(max(a[l - 1 : r]), a.index(max(a[l - 1 : r])) + 1)