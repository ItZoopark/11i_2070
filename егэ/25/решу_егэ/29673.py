# не для больших чисел
# from math import ceil
# for x in range(0, 1000000):
#     lst = []
#     for i in range(2, ceil(x**0.5)+1):
#         if x % i == 0:
#             lst.append(i)
#             if i != x // i:
#                 lst.append(x // i)
#
#             if len(lst) > 3:
#                 break
#     if len(lst) == 3:
#         print(lst)

a = 123456789
b = 223456789

start = int(a**0.25)+1
while start**4 < b:
    start+=1
    for i in range(2, int(start**0.5)+1):
        if start % i == 0:
            break
    else:
        print(start**4, start**3)

