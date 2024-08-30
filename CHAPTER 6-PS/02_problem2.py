a = int(input("ENTER THE MARKS: "))
b = int(input("ENTER THE MARKS: "))
c = int(input("ENTER THE MARKS: "))

if(a < 33 or b < 33 or c < 33):
    print("FAIL")

elif((a + b + c) / 3 < 40):
    print("FAIL")

else: 
    print("PASS")