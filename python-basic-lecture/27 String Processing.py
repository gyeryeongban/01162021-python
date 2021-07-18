'''text=input('text:')

for i in text:
    if i !=' ':
        print(i,end='')



text=input('text:')

for i in text:
    if i.isupper():
        print(i.lower(),end='')
    elif i.islower():
        print(i.upper(),end='')
    else:
        print(i,end='')'''



name=['배타미','송가경','차현','가나다']

'''for i in name:
    if '가' in i:
        print(i)'''

for i in name:
    if i[0]=='배':
        print(i)
