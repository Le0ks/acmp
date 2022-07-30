a, b = map(int, input().split())
print((a % b + abs(b)) % abs(b))