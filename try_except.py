result = input("Enter your marks: ")
try:
    marks = float(result)
    if marks >= 0.0 and marks <= 1.0:
        if marks >= 0.9:
            print("A")
        elif marks >= 0.8:
            print("B")
        elif marks >= 0.7:
            print("C")
        elif marks >= 0.6:
            print("D")
        elif marks <= 0.6:
            print("F")
        else:
            print("Bad score")
    else:
        print("Bad score")
except:
    print("Please enter a valid number")