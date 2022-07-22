# faulty calculator
#Design a calculator which will correctly solve all the problems except these:  45 *3 = 555, 56+9 = 77, 56/6 = 4
#program should take operator and the two inputs from th user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oper = input("Select any from the given operators: *,/,+,- : ")

if (num1 == 45 and num2 == 3 and oper == "*") or (num1 == 3 and num2 == 45 and oper == "*") :
    print("555")
elif (num1 == 56 and num2 == 9 and oper == "+") or (num1 == 9 and num2 == 56 and oper == "+"):
    print("77")
elif (num1 == 56 and num2 == 6 and oper == "/") :
    print("4")
elif oper == "*" :
    print("Multiplication is: ",(num1*num2))
elif oper == "+" :
    print("sum is: ",(num1+num2))
elif oper == "-" :
    print("Substraction is: ",(num1-num2))
elif oper == "/" :
    print("Division is: ",(num1/num2))
else:
    print("Please recheck your input")
