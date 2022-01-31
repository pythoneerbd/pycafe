marks = float(input("Enter your marks: "))

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
