for x in range(174457, 174505 + 1):
    lst = []
    for i in range(2, x//2+1):
        if x % i == 0:
            lst.append(i)
            if len(lst) > 2:
                break
    if len(lst) == 2:
        print(lst)
