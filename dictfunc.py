def display(**kwargs):
    print("Record Information")
    for k,v in kwargs.items():
        print(k,"______________",v)
        
display(name="Waseem",marks=100,age=35)
