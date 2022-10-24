# не для больших чисел
# from math import ceil
# a = 123_456_789
# b = 223_456_789
# for x in range(a, b):
#     lst = []
#     for i in range(2, ceil(x**0.5)):
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

p = 2
while p ** 4 <= b:
    if p ** 4 >= a:
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                break
        else:
            print(p ** 4, p ** 3)
    p += 1

# start = int(a**0.25)+1
# while start**4 < b:
#     start+=1
#     for i in range(2, int(start**0.5)+1):
#         if start % i == 0:
#             break
#     else:
#         print(start**4, start**3)
