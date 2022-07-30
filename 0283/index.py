n = input()
ans = 0
a = 0
while n:
  if n[a].isupper() and n[a + 1].islower() and len(n) >= 2:
    if n[a + 2].isupper() and len(n) == 2:
      ans += 1
      n = n[a + 2:]
      break
    elif n[a + 2].isupper() and len(n) > 2:
      ans += 1
      n = n[a + 2:]
  elif n[a].isupper() and n[a + 1].islower() and n[a + 2].islower() and len(n) >= 3:
    if n[a + 3].isupper() and len(n) == 3:
      ans += 1
      n = n[a + 3:]
      break
    elif n[a + 3].isupper() and len(n) > 3:
      ans += 1
      n = n[a + 3:]
  elif n[a].isupper() and n[a + 1].islower() and n[a + 2].islower() and n[a + 3].islower() and len(n) >= 4:
    if n[a + 4].isupper() and len(n) == 4:
      ans += 1
      n = n[a + 4:]
      break
    elif n[a + 4:].isupper() and len(n) > 4:
      ans += 1
      n = n[a + 4:]
  else:
    ans = 0
    break
if ans > 0:
  print('Yes')
else:
  print('No')
