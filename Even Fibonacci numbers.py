#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
a1=1
a2=2
sum1=0
sum2=0
while a2<4*10**6:
    if a1%2==0:
        sum1=sum1+a1
    if a2%2==0:
        sum2=sum2+a2
    a1=a1+a2
    a2=a1+a2
sum0=sum1+sum2
print(sum0)
