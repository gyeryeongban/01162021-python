'''print('a가 0보다 같거나 크면 실행, 작으면 정지')
a=int(input('a:'))
while a>=0:
    print('실행')
    a=int(input('a:'))
a=10
while a>0:
    print('실행')
n=int(input('n:'))
while n:
    print(n)
    n=n-1
n=1
while n<=10:
    print(n)
    n=n+1
text='yes'
while text=='yes':
    text=input('yes 입력 시 반복')
print('종료')'''
text=input('e 또는 E 입력 시 종료')
while text!='e' and text!='E':
    text=input('e 또는 E 입력 시 종료')
print('종료')
