b=1
c=0
L=[]
result=1
def zarib(x):
   for i in range(2,int(x)+1):
       if x%i==0:
           x=x/i
           return i

for i in range(1,21):
   b=b*i
   
for j in range(1,100):
   if zarib(b)>=c:
       c=zarib(b)
       L.append(c)
   b=b/zarib(b)
   if b==1.0:
       break


for z in set(L):
   result=result*z

print(result)
