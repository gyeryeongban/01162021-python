'''age=int(input('나이 입력:'))
if age<=7:
    print('유아입니다.')
elif age<=19:
    print('청소년입니다.')
    if age<=13:
        print('초등학생')
    elif age<=16:
        print('중학생')
    else:
        print('고등학생')
else:
    print('성인입니다.')
n=int(input('n:'))
for i in range(1,n+1):
    if i%3==0:
        print('X')
    else:
        print(i)
num1=0
num2=int(input('n:'))
while True:
    num1=num1+1
    print(num1)
    if num1==num2:
        break'''
for i in range(1,7):
    for j in range(1,7):
        print(i,j)
