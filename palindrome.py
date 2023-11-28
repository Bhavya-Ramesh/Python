def palindrome():
    n=int(input("enter a value:"))
    org=n
    sum=0
    while(n>0):
        a=n%10
        sum=sum*10+a
        n=n//10
        if(sum==org):
            print("palindrome")
        else:
            print("not palindrome")
palindrome()
