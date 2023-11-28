def max_guest(enter,leave,T):
    max_guest=0
    current_guest=0
    for i in range(T):
        current_guest+=enter[i]-leave[i]
        max_guest=max(max_guest,current_guest)
    return max_guest
enter=[12]
leave=[10]
T=1
result = max_guest(enter,leave,T)
print(result)


