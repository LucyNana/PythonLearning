largest = 0
smallest = 100


# ------------> Start of While Loop
while True:
    #Step 1. Read Input, valid input number
        n = input("Enter a number:")
        if n == "done":
            break
        try:
            n= float(n)
        except:
            print("Invalid input")
            continue

    # Step 2. If it valid accumulate count and its sum
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
# ------------> End of While Loop

print("Maximun is ",largest)
print("Smallest is ", smallest)
