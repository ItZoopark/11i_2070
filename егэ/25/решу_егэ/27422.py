from math import ceil
for x in range(174457, 174505 + 1):
    lst = []
    for i in range(2, ceil(x**0.5)):
        if x % i == 0:
            lst.append(i)
            lst.append(x // i)
            if len(lst) > 2:
                break
    if len(lst) == 2:
        print(lst)
