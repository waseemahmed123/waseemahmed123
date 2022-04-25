def fact(n):
    x=1
    while n>=1:
        x=x*n
        n=n-1
    return x
print(fact(4))


for i in range(1,6):
    print("factorial of {} is: {}".format(i,fact(i)))
        
        
