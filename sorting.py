# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(0, n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# # Get list input from user
# user_input = input("Enter a list of numbers separated by spaces: ")
# arr = [int(x) for x in user_input.split()]

# print("Array before sort: ", arr)
# arr = bubble_sort(arr)
# print("Array after sort is: ", arr)
def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1;
        while j>=0 and key<arr[j] :
            arr[j+1]=arr[j]
            j=j-1
    arr[j+1]=key
    return arr
arr = input("Enter a list of number separated by space : ")
arr1=[int(x) for x in arr.split()]
print("Array before sort : ",arr1)
arr2=insertion(arr1)
print("Array after sort is : ",arr2)