'''text=input('text:')
t=input('t:')

check=False

for i in text:
    if i == t:
        check=True
        
print(check)'''


li=list(map(int,input('li:').split()))
n=int(input('n:'))

'''check=False

for i in li:
    if i == n:
        check=True
        
print(check)'''

print(n in li)
