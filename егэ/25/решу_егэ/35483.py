a = 35_000_000
# a = 35_819_000
# a = 38_950_081
# a = 39037448
b = 40_000_000

from math import ceil

for x in range(a, b):
    lst = []
    for i in range(1, ceil(x ** 0.5) + 1):
        if x % i == 0:
            lst.append(i)
            if i != x // i:
                lst.append(x // i)

    count = 0
    for el in lst:
        if el % 2 != 0:
            count += 1
    if count == 5:
        print(x)
        # print(lst)

# start = int(a ** 0.25)
# while start ** 4 < b:
#     start += 1
#     if start % 2 != 0:
#         for i in range(2, int(start ** 0.5) + 1):
#             if start % i == 0:
#                 break
#         else:
#             p = 0
#             while (start ** 4) * (2 ** p) < b:
#                 print(start ** 4 * 2 ** p)
#                 p += 1

# 35819648
#
# 38950081
#
# 39037448
#
# 39337984
