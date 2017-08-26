ext = "X-DSPAM-Confidence:    0.8475";

#--> find the location of the starting & ending letter
a = ext.find('0')
b = ext.find('5')

host = ext[a : b+1 ]
print(float(host))
