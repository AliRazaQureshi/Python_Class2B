def ADD(a,b):
    result = a + b
    return result

def SUB(a,b):
    result = a - b
    return result

def MULT(a,b):
    result = a * b
    return result

def DIV(a,b):
    result = a / b
    return result

def POWER(a,b):
    result = a ** b
    return result

def main():
    print("Select Operation: +, -, *, /, pow")

    op = input("Enter the Operation: ")

    if op == "+":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = ADD(a,b)
        print("{} + {} = {}".format(a,b,result))

    elif op == "-":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = SUB(a,b)
        print("{} - {} = {}".format(a,b,result))

    elif op == "*":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = MULT(a,b)
        print("{} * {} = {}".format(a,b,result))

    elif op == "/":
        a = float(input("Enter divisor: "))
        b = float(input("Enter divident: "))
        result = DIV(a,b)
        print("{} / {} = {}".format(a,b,result))

    elif op == "pow":
        a = float(input("Enter number: "))
        b = float(input("Enter power: "))
        result = POWER(a,b)
        print("{} ** {} = {}".format(a,b,result))

    else:
        print("Wrong Operation")

while True:
    main()