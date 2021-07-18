'''n=int(input('n:'))
s=0

for i in range(1,n+1):
    s=s+i

print(s)



n=int(input('n:'))
s=1

for i in range(1,n+1):
    s=s*i

print(s)'''



n=int(input('n:'))
s=0

while n!=0:
    s=s+n
    n=int(input('n:'))

print(s)
