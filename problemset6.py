# # a = int(input("Enter your agge : "))
# # if(a>=18) :
# #     print("Yes")
# # else :
# #     print("No")

# # Answer 1
# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))
# d = int(input("Enter 4th number : "))
# if(a>b and a>c and a>d) :
#     print(f"{a} is the greatest of all")
# elif( b>c and b>d) :
#     print(f"{b} is the greatest of all")
# elif(c>d) :
#     print(f"{c} is the greatest of all")
# else :
#     print(f"{d} is the greatest of all")

# # Answer 2
# a = int(input("Enter your marks in math : "))
# b = int(input("Enter your marks in physics : "))
# c = int(input("Enter your marks in chemistry : "))

# total = (100*(a+b+c))/300

# if(a>=33 and b>=33 and c>=33) :
#         if(total>=40) :
#             print("You are pass")

# Answer 3
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# comment = input("Enter your comment here : ")

# if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)) :
#     print("You are spammer")
# else :
#     print("Not spammer")

# Answer 4
# name = input("Enter your name : ")
# count =0
# for i in name :
#     count += 1
# if(count<10) :
#      print("Your name has ",count ," letters")
# else : 
#    print("Your name has ",count," letters long")

# Answer 5
# list = ["Dhrumil","Dhruv","Thakar","Godfather","Waanted"]
# if("Dhrumil" in list) :
#     print("yes")
# else :
#     print("No")

# Answer 6
Marks = int(input("Enter your marks : "))
if(Marks>=90 or Marks<=100) : 
    print("Grade Ex")
elif(Marks>=80 or Marks<=90) :
    print("Grade A")
elif(Marks>=70 or Marks<=80) :
    print("Grade B")
elif(Marks>=60 or Marks<=70) :
    print("Grade C")
elif(Marks>=50 or Marks<=60) :
    print("Grade D")
elif(Marks<=50) :
    print("Grade F")
else :
    print("Invalid marks")