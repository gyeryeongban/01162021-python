'''n=int(input('n:'))

a=3

for i in range(n-1):
    a=a+5

print(a)



n=int(input('n:'))

a=3

for i in range(n-1):
    a=a*2

print(a)



n=int(input('n:'))
a=int(input('a:'))
r=int(input('r:'))


for i in range(n-1):
    a=a*r

print(a)'''




n=int(input('n:'))

a=1
b=2

for i in range(n-2):
    c=a+b
    a=b
    b=c

print(b)
