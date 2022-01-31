def calculate(a,b):
    if operator == '+':
        added = a + b
        return added
    elif operator == '-':
        subs = a - b
        return subs
    elif operator == '*':
        multi = a * b
        return multi
    elif operator == '/':
        divi = a / b
        return divi
    elif operator == '//':
        floo = a // b
        return floo
    elif operator == '%':
        modu = a % b
        return modu
    else:
        print("please enter correct operator")
        
a = int(input("Enter first number: "))
operator = str(input("select + - * // %: "))
b = int(input("Enter calculate number: "))
x = calculate(a, b)
print(x)