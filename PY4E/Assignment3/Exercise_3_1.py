hrs = input("Enter hours:")
rate = input("Enter rate per hour:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Pls enter numeric number")
    quit()

if h <= 40:
    pay = h*r
else:
    pay = 1.5*(h-40)*r + 40*r
print(pay)
