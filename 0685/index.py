a1, a2, a3, b1, b2, b3 = map(int, input().split())
max_price = max(a1, a2, a3)
max_weight = max(b1, b2, b3)
min_price = min(a1, a2, a3)
min_weight = min(b1, b2, b3)
sr_price = a1 + a2 + a3 - max_price - min_price
sr_weight = b1 + b2 + b3 - max_weight - min_weight
print(max_price * max_weight + sr_price * sr_weight + min_price * min_weight)
