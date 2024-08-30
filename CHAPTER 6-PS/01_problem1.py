a = int(input("ENTER THE 1ST NUMBER: "))
b = int(input("ENTER THE 2ND NUMBER: "))
c = int(input("ENTER THE 3RD NUMBER: "))
d = int(input("ENTER THE 4TH NUMBER: "))

if(a > b and a > c and a > d):
    print("GREATEST NUMBER IS A: " , a)

elif(b > a and b > c and b > d):
    print("GREATEST NUMBER IS B: " , b)

elif(c > a and c > b and c > d):
    print("GREATEST NUMBER IS C: " , c)

else:
    print("GREATEST NUMBER IS D: " , d)


