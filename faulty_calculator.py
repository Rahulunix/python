#45*3 = 555, 56+9 = 77, 56/6 = 4
#Faulty calculator
num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
oper = input("enter the operator +,/,*,-,% ")
if num1 == 45 and num2 == 3 and oper == "*" :
    print(" 555")
elif num1 == 56 and num2 == 9 and oper == "+" :
    print(" 77")
elif num1 == 56 and num2 == 6 and oper== "/"  :
    print(" 4 ")
elif oper == "-" :
    subt = num1 - num2
    print(subt)
elif oper == "+":
    add = num1 + num2
    print(add)
elif oper == "*":
    mult = num1 * num2
    print(mult)
elif oper == "%":
    modu = num1 % num2
    print(modu)
elif oper == "/":
    div = num1 / num2
    print(div)
else :
    print("Error please recheck your entry")


