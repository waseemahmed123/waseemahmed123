def f1():
    def inner(a,b):
        print("The sum:",a+b)
        print("The avg:", (a+b)/2)
    inner(10,20)
    inner(20,30)
    inner(40,50)
    inner(100,200)

f1()    
