a,b,c,d,e=[int(x)for x in input("enter rows in rectangle:").split(" ")]
l=(a,b,c,d,e)

for i in l:
    for j in l:
      print("* ",end=" ")
    print()

n=int(input("Enter the number of rows"))

for i in range(1,n+1):
    for j in range(1,i+1):
      print("* ",end=" ")
    print()
        
          
