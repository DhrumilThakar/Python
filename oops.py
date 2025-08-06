class student:
    subject = "Python"
    marks=100
    def about(self):
        print(f"Name: {self.name}, Subject: {self.subject}, Marks: {self.marks}")
    def __init__(self):
        print("This is a dunder method")#This is a constructor it is called automatically when a object is created
    @staticmethod
    def greet():
        print(f"Hello, :)")


dhrumil = student()
print(dhrumil.subject,dhrumil.marks)
dhrumil.name="Dhruv" #This is called object attribute or instance attribute
print(dhrumil.name,dhrumil.subject,dhrumil.marks)
# Here name is object attribute and marks and subject are class attribute
""" Note: Instance attributes, take preference over class attributes during assignment & 
retrieval. """
print(dhrumil.about())
print(dhrumil.greet())
def __str__(self):
    return f"Name: {self.name}, Subject: 
