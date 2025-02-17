lst = [1,2,3,4,5,6,7,8,9]
#
# def get_lement_by_index(lst, index):
#     return lst[index]
#
# print(get_lement_by_index(lst=lst, index=4))
#
# lst2 = [9,2,21,6,83,1,8,]
# def binary_search(lst, target):
#     left, right = 0, len(lst) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#              right = mid - 1
#     return -1
#
# print(binary_search(lst,9))

# def find_lement(lst, target):
#     for i in lst:
#         if i == target:
#             return True
#
#     return False
#
# print(find_lement(lst,10))

lst3 = [9,2,5,1,5,2,8,7,45]

def bubble_sort(lst):
    n = len(lst)
    print("for 1" + range(n))
    for i in range(n):
        print(i)
        print("for 2--", range(n - i - 1))
        print('for 3---', j)

        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

bubble_sort(lst = lst3)
print(lst3)