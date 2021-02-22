'''li=list(map(int,input('Enter Number:').split()))

m=li[0]

for i in li:
    if i<m:
        m=i
        print(m)'''



li=list(map(int,input('Enter Number:').split()))

m=li[0]

for i in li:
    if i>m:
        m=i
        print(m)
