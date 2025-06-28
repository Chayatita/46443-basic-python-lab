celsius = int(input("Enter temperature: "))
if (celsius <= 0):
    print ("Freezing")
elif (celsius >=1 and celsius < 16):
    print ("Cold")
elif (celsius >=16 and celsius < 31):
    print("Warm")
elif (celsius >30):
    print("Hot")