# def greet() :
#     print("Hello")
# greet()

"""Answer 1"""
# def great(a,b,c):
#     if a>b and a>c :
#         print("a is greater then the 2")
#     elif b>a and b>c:
#         print("b is greater then the 2")
#     else :
#         print("c is greeater then 2")

# great(5,6,7)

"""Answer 2"""
# def converter(c):
#     f=(c*1.8)+32
#     return f
# a = float(input("Enter the celsius degree : "))
# print(converter(a))

"""Answer 3*"""
"""By adding end and assiging it null we can prevent print function to print new line at the end"""
# print("Hello",end="")

"""Answer 4"""
# def sum(n):
#     if n==1 or n==0:
#         return 1
#     return n+sum(n-1)
# a=int(input("Enter the integer : "))
# print(f"Sum of first {a} number is {sum(a)}")

"""Answer 5"""
# def pattern(n):
#     for i in range(1,n+1):
#         print("*"*n,end="")
#         print()
#         # n=n-1
# pattern(3)

"""Answer 6"""
# def co(inches) :
#     cm=inches*2.54
#     return cm
# a=float(input("Enter the lenght in inches : "))
# print(f"The length in cm is {co(a)}")

"""Answer 7"""
# def r(list,word):
#     for i in list:
#         if i==word:
#             a=list.remove(word)
#     return list
# list=["apple","banana","cherry","date","elderberry"]
# print(r(list,"banana"))

"""Answer 8"""
# def table(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
# a= int(input("Enter the number to find the table : "))
# table(a)