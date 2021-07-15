num=int(input("enter 4 Digit Number"))
total=0
total=total+num%10
num=num//10 
total=total+num%10
num=num//10 
total=total+num%10
num=num//10 
total=total+num%10
num=num//10 
print("Total of digits ", total)
