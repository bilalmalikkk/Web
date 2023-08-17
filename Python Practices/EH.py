
try:
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    def average(num1,num2):
        average=int((num1+num2))/2
        return average
    print(average(num1,num2))

except Exception as e:
    print("enter the right input")
    print(e)
else:
    print("Rest of the Code")

finally:
    print("Finally")





Flag=True
while(Flag):
    try:
        num1=int(input(("Enter num1: ")))
        num2=int(input(("Enter num2: ")))
        num3=int(input(("Enter num3: ")))
        a=int((num1+num2)/num3)
        print(a)
        Flag=False
    except:
        print("Enter the right input: ")
