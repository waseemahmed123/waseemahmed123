numbers=[10,20,0,5,0,30]
for n in numbers:
    if n==0:
     print("infinity")
     continue
    else:
     print("100/{}={}".format(n,100/n))
