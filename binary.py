def binary(arr,key):
    a = len(arr)
    for i in range (0,a):
        if arr[i] == key:
            return i
    return -1

user_input = input("Enter the array : ")
arr = [int (x) for x in user_input.split()]
print("Array befor sort is : ",arr)
arr1 = binary(arr,5)
print("Array after sort is : ",arr1)