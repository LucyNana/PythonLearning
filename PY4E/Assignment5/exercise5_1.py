count = 0
sum = 0
n = 0

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
        sum = sum + float(n)
        count = count + 1
# ------------> End of While Loop

print("Done")
print("Sum:",sum)
print("Count:",count)
print("Average:",sum/count)
