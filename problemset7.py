# Answer 1

# number = int(input("Enter the number : "))
# for i in range(1,11) :
#     print(number," * ",i," = ",number*i)

# Answer 2

# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for i in l :
#     if(i.startswith("S")) :
#         print(f"Kem cho {i}")

# Answer 3

# number = int(input("Enter the number : "))
# i = 1
# while i<=10 :
#     print(number," * ",i," = ",number*i)
#     i+=1

# Answer 4

# num = int(input("Enter the number : "))
# count =0
# for i in range(1,num) :
#     if(num%i==0) :
#         count+=1
# if(count == 2):
#     print("Enter number is prime !")
# else:
#     print("Enter number is not prime !")

# Answer 5

# n = int(input("Enter the number : "))
# i=0
# sum = 0
# while i<=n :
#     sum +=i
#     i+=1
# print("Sum of first ",n," natural number is :-",sum)

# Answer 6

# n = int(input("Enter the number : "))
# product =1
# for i in range (1,n+1) :
#     product *= i
# print("The factorial of ",n," is :-",product)

# Answer 7 imp

# n = int(input())
# for i in range(1,n+1) :
#         print(" "*(n-i),end="")
#         print("*"*(2*i-1),end ="")
#         print(" ")

# Answer 8 

# n = int(input())
# for i in range(1,n+1) :
#     print("*"*i,end ="")
#     print()
    
# Answer 9

"""
* * * 
*   *   for n = 3 
* * * 

"""
# n = int(input())

# for i in range (1,n+1) :
#     if(i==1 or i==n) :
#         print("*" *n,end="")
#     else :
#         print("*",end ="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

# Answer 10

n = int(input("Enter the number : "))
for i in range(1,11) :
    print(n," * ",11-i," = ",n*(11-i))