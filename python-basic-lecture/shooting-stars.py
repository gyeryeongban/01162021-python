'''n=int(input('n:'))

for i in range(n):
    print(' '*i,end='')
    print('*'*n)



n=int(input('n:'))

for i in range(1,n+1):
    print('*'*i)



n=int(input('n:'))

for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*i)



n=int(input('n:'))

for i in range(n):
    print('*'*(n-i))



n=int(input('n:'))

for i in range(n):
    print(' '*i,end='')
    print('*'*(n-i))'''



n=int(input('n:'))

for i in range(n):
    print(' '*(n-i-1),end='')
    print('*'*(i*2+1))
