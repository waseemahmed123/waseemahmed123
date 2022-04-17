cart=[10,20,600,70,90]
for items in cart:
    if items>500:
        print("PROCESSIG ITEMS",items)
        print("sorry cannot process this item")
        continue
    else:
      print("congrats")
      print("PROCESSIG ITEMS",items)
