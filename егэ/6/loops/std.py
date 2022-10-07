x = range(0, 101) # 0..100

s = 0
count = 0
for xi in x:
    s += xi
    count += 1

m = s / count

s = 0
for xi in x:
    s += (xi - m)**2

res = (s / count)**0.5
print(res)