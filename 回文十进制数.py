
# def ten_to_other(nums, n):
#     res = []
#     while nums > (n-1):
#         res.append(nums % n)
#         nums = nums // n
#     res.append(nums)
#     res = map(str, res)
#     return ''.join(res)
#
# def isBackText(num):
#     n = str(num)
#     return n[::-1] == n
#
# # print(ten_to_other(9, 2))
#
# n = 10
# while 1:
#     if isBackText(n):
#         num_2 = ten_to_other(n, 2)
#         num_8 = ten_to_other(n, 8)
#         if isBackText(num_2) and isBackText(num_8):
#             print(n)
#             break
#     n += 1

n = 11
while 1:
    num_2 = '{0:b}'.format(n)
    num_8 = '{0:o}'.format(n)
    if str(n)[::-1] == str(n) and num_2[::-1] == num_2 and num_8[::-1] == num_8:
        print(n)
        break
    n += 2