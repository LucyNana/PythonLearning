hrs = input("Enter the hours:")
rate = input("Enter the rate:")
h = float(hrs)
r = float(rate)

def computepay(pay):
    if h > 40:
        pay = 1.5*h*r
    else:
        pay = h*r
    return pay

x = computepay('pay')
print(x)
