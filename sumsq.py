def sumsquare():
    odd=0
    even=0
    list=[1,4,9,12,13,40,18]
    for a in list:
        if a%2!=0:
            odd+=a**2
        else:
                even+=a**2
                print(odd,even)
sumsquare()
    
