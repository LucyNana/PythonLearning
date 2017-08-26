score = input("Enter score:")
s = float(score)
if s < 0.6:
    print("F")
elif s >= 0.6 and s < 0.7:
    print("E")
elif s >=0.7 and s < 0.8:
    print("C")
elif s >= 0.8 and s < 0.9:
    print("B")
elif s >= 0.9:
    print("A")
