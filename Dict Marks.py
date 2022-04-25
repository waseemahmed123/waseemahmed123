#for finding student marks
n=int(input("enter the number of students:"))

d={}
for i in range(n):
      name=input("Enter student name:")
      marks=int(input("Enter student marks:"))
      d[name]=marks
print(d)
while True:
    name=input("enter student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("student not available")
    else:
        print("The marks of {}:{}".format(name,marks))
       
    option=input("do you want to find another student marks[Yes|No]:")     
    if option=="No":
         break
print("Thanks for using our application")     
