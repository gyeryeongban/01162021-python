'''n=int(input('n:'))

#check=0
li=[]

for i in range(1,n+1):
    if n%i==0:
        #check=check+1
        li.append(i)

#print(check)
print(len(li))



text=list(input('text:'))

#print(text.count('o'))
#print(text.count('x'))

o_count=0
x_count=0

for i in text:
    if i=='o':
        o_count=o_count+1
    elif i=='x':
        x_count=x_count+1

print(o_count)
print(x_count)'''



num=list(map(int,input('num:').split()))

avg=sum(num)/len(num)

check=0

for i in num:
    if i>=avg:
        check=check+1

print(avg)
print(check)
