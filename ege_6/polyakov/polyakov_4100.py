max = -float("inf")
min = float("inf")
for s in range(1000):
    s1 = s
    n = 600
    while n > s1:
        s1 = s1 + 3
        n = n - 6
    if n == 210:
      if s > max:
        max = s
      if s < min:
        min = s

print(max, min)