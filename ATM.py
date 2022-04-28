print("welcome to Bank")
restart=("y")
chances=3
balance=10000
while chances>=0:
    pin=int(input("Please enter 4 digit pin:"))
    if pin==(1234):
        print("you entered your pin correctly\n")
        while restart not in("n","no","NO","N"):
               print("Please print 1 for you Balance\n")
               print("Please press 2 to make withdrawl\n")
               print("Please press 3 to pay in\n")
               print("Please press 4 to Return Card\n")
               option=int(input("what would you like to choose:"))
               if option==1:
                   print("your Balance is :", balance,"\n")
                   restart=input("would you like to go back?")
                   type(restart)
                   if restart in ("n","NO" ,"no","N"):
                       print("Thankyou")
                       break
               elif option==2:
                   option2=("y")
                   withdrawl=float(input("How much would you like to withdraw?"))
                   if withdrawl in [100,200,500,2000]:
                       balance = balance-withdrawl
                       print("Your balance is now", balance)
                       restart=input("would you like to go back?")
                       print(type(restart))
                       if restart in ("n","NO","no","N"):
                           print("Thankyou")
                           break
                       elif withdrawl!=[100,200,500,2000]:
                           print("Invalid Amount, Please re-try\n")
                           restart-("y")
                       elif withdrawl==1:
                           withdrawl=float(input("Please enter desired amount:"))
               elif option==3:
                   Pay_in=float(input("How munch would you like to pay in:"))
                   balance=balance+Pay_in
                   print("\nYour balance is now",balance)
                   restart=input("would you like to go back?")
                   if restart in ("no","n","NO","N"):
                       print("thankyou")
                       break
               elif option==4:
                 print("Please wait your card is Returned....\n")
                 restart=("y")
                           
    elif pin!=(1234):
        print("incorrect password")
        chances=chances-1
        if chances==0:
            print("\nNo more tries")
            break







