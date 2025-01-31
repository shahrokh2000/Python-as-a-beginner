n=0
for i in range(999,99,-1):
    for j in range(i,99,-1):
        a=i*j
        s=str(a)
        if s==s[::-1]:
            #print(i,'*',j,'=',s)
            if a>n:
                n=a
print(n)
