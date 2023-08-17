Anumber = "ATM000"
class AccountNotFound(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class InvalidPin(Exception):
    pass


def AccountNo(anum):
    global Anumber
    Anumber = anum
    temp=int(Anumber[3:])
    temp += 1
    temp = str(temp)
    if (len(temp) == 1):
        Anumber = "ATM00" + temp
    if (len(temp) ==2):
        Anumber = "ATM0" + temp
    if (len(temp)==3):
        Anumber=temp
    return Anumber


def registerAccount():
    global Anumber
    AccNo=AccountNo(Anumber)
    Anumber = AccNo
    Flag=True
    while Flag == True:
        try:
            password=int(input("Enter pass: "))
            password=str(password)
            if len(password) != 4:
                raise InvalidPin("Password should contain 4 letters!")
            else:
                Flag=False
        except InvalidPin as e:
            print(str(e))

        AccountBalance=100
        Anumber=str(Anumber)
        AccountBalance=str(AccountBalance)
        with open("atmData.txt", "a+") as f:
            f.write(Anumber)
            f.write(",")
            f.write(password)
            f.write(",")
            f.write(AccountBalance)
            f.write("\n")
            r=[]
            r1=f.readline()
            r.append(r1)

    
registerAccount()

def Login():
    with open("atmData.txt","r") as f:
        print("Enter the Account No:")
        Ac=input()
        print("Enter the Password:")
        Ps=input()
        listdata = []
        flag = True
        for i in f.readlines():
            str1 = i.split(",")
            if flag == True:
                if Ac==str1[0]:
                    if Ps==str1[1]:
                        print("Successfully Login!")
                        num = int(input("Enter 1 for print balance\nEnter 2 for withdraw cash\nEnter 3 for deposit Cash\n"))
                        if num == 1:
                            print("user curent balance is: ", str1[2])
                        elif num == 2:
                            withdraw = int(input("Enter the amount you want to withdraw: "))
                            if withdraw < 0:
                                raise InsufficientBalance("Amount can not be negative")
                            elif withdraw > int(str1[2]):
                                raise InsufficientBalance("Amount can not exceede from current balance ")
                            else:
                                str1[2] = str(int(str1[2]) - withdraw)
                        elif num == 3:
                            deposit = int(input("Enter the number of amount to be deposited: "))
                            if deposit < 0:
                                raise InsufficientBalance("Amount can not be negtive ")
                            else:
                                str1[2] = str(int(str1[2]) + deposit)
                    flag = False
                else:
                    print("Account don't exist!\nKindly register first")
            listdata.append(str1)
        # print(listdata)
        # for f in Data:
        #     print(f)

Login()
    







    



