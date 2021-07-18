'''a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

for i in range(1,a+1):
    for j in range(1,b+1):
        if i+j==c:
           print(i,j)



for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j))
    print()'''



li=[[1,2,3,4],[5,6,7,8]]

for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j],end=' ')
    print()
