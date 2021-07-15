num=int(input("enter 4 Digit Number"))
rev=0
rev=rev*10+num%10
num=num//10 
rev=rev*10+num%10
num=num//10 
rev=rev*10+num%10
num=num//10 
rev=rev*10+num%10
num=num//10 
print("Reverse of digits number is ", rev)
