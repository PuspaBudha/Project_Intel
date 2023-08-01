import time
print("Please Insert your Card")
time.sleep(5)
pin = int(input("Enter your 4 digit ATM Pin"))
Balance = 100000
if pin == 1234:
    while True:     
        print("1 = Check Balance")
        print("2 = Withdraw money")
        print("3 = Deposite Money")
        print("4 = exit")
        try:
            option=int(input('Chose any option above'))
        except:
            print("Please Choose the valid option")
        if option==1:
                print('---------------')
                print(f"Your current Balance is {Balance}")
        if option ==2:
            withdraw_money=int(input("Enter the withdraw Amount"))
            if withdraw_money>10000:
                print("Your amount is more than 10000 so, Scan your Finger Print")
            else: 
             if withdraw_money<Balance:
               Balance = Balance- withdraw_money
            print("---------------")
            print(f"your current balance is {Balance}")
            print("--------")
        if option==3:
            deposite_money=int(input("Enter the Deposite Amount"))
            Balance = Balance + deposite_money
            print("-------------")
            print(f"{deposite_money}is credit to your Amount")
        if option==4:
            print("Thank you for visiting our ATM Machine...See you again")
            break
else:
    print("You Entered the Wrong Password...Please Try Again")