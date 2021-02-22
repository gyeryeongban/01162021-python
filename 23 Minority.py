'''n=int(input('n:'))

check=True

for i in range(2,n):
    if n%i==0:
        check=False

if check==2:
    print(True)
else:
    print(False)

print(check)'''

    

a=int(input('a:'))

li=[]

for n in range(2,a+1):
    check=True
    for i in range(2,n):
        if n%i==0:
            check=False
    if check:
        li.append(n)
