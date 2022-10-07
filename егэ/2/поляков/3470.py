print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x and (y or not z) and w) == (x <= (not y and z))
                if f == 1:
                    print(x, y, z, w)