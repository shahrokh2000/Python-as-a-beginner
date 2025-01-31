def factor(a):
    for i in range(2,int(a+1)):
        if a%i==0:
            a=a/i
            break
    return i

b=int(input('Largest prime factor:'))
c=0
for j in range(1,100):
    if factor(b)>=c:
        c=factor(b)
    b=b/factor(b)
    if round(b)==1:
        break
print(c)
