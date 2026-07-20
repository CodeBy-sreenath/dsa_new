n=int(input("enter the number"))
isprime=True
if n==0 or n==1:
    print("not a prime nor a not prime")
elif n==2:
    print("prime number")
else:
    i=2
    while i<=n//2:
        if n%i==0:
            isprime=False
        i+=1
    if isprime:
        print("prime number")
    else:
        print("not a prime number")            
                