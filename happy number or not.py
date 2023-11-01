num=int(input("Enter a number:"))
sum=0
while sum != 1 and sum != 4:
    sum=0
    while num!=0:
        rem = num % 10
        sum += (rem*rem)
        num //= 10
    num=sum

if sum==1:
    print("It is a Happy Number.")
else:
   print("It is  an Unhappy Number.")
