'''a=int(input('a:'))
b=int(input('b:'))

if b%a==0:
    print('배수입니다.')
else:
    print('배수가 아닙니다.')


n=int(input('n:'))

for i in range(1,n+1):
    if n%i==0:
        print(i)'''


n=int(input('n:'))

for i in range(1,101):
    if i%n==0:
        print(i)
