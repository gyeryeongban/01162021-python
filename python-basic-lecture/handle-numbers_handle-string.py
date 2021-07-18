'''
a=int(input('a enter:'))
b=int(input('b enter:'))
c=int(input('c enter:'))
print(a,b,c,a+b+c)
'''
'''
a,b,c=map(int,input('a b c enter:').split())
print(a,b,c,a+b+c)
'''
'''
text=input('Enter Date: mm.dd.yyyy')
m,d,y=text.split('.')
print(text,m,d,y)
'''
'''
a,b,c=map(int,['1','2','3'])
print(a,b,c,a+b+c)
'''
'''
a,b,c=map(int,input('Enter a b c:').split())
text=input('Enter a b c:')
text=text.split()
a,b,c=map(int,text)
print(a,b,c,a+b+c)
'''
'''
x=2
y=1
print(x,y,x+y)
print('1과 2의 합은 3이다.')
print(str(x)+'과'+str(y)+'의 합은'+str(x+y)+'이다.')
'''
'''
print(x,end='')
print('과 ',end='')
print(y,end='')
print('의 합은 ',end='')
print(x+y,end='')
print('이다.')
'''
'''
print('{}과 {}의 더하기는 {}이다.'.format(x,y,x+y))
print(str('{}과 {}의 빼기는 {}이다.'.fomat(x,y,x-y)
print('{}과 {}의 곱하기는 {}이다.'.fomat(x,y,x*y))
print('{}과 {}의 나누기는 {}이다.'.fomat(x,y,x/y))
'''
'''
print(round(2.62))
print(round(4.54))
print(round(2.26,1))
'''
'''
print(abs(9))
print(abs(-9))
'''
#print(pow(6,9))
#print(6**9)
'''x,y=divmod(9,3)
print(x)
print(y)
'''
'''print(max(1,2,3,4))
print(min(1,2,3,4))
print(sum([1,2,3,4]))'''
'''text='abc'
print(text[-3])
print(text[-2])
print(text[-1])'''
text='abc def ghi jkl mno'
#print(text[3:8])
#print(text[-3:-1])
'''print(text[6:])
print(text[:6])
print(text[:])
print(text[::-1])'''
'''text='You {} {}'
print(text.format('are',19))'''
'''text='I am women'
print(text.replace('women','men'))'''
'''text='abcde A/B/C A.B.C'
a,b,c=text.split('/')
print(a)
print(b)
print(c)'''
'''text='clean'
print('/'.join(text))
text='What do you want me to pay for you?'
print(text.count('w'))
print(text.count('o'))
print(text.count('a'))
text='$$$wo$men$$$'
print(text.strip('$'))
print(text.lstrip('$'))
print(text.rstrip('$'))
text='women women'
print(text.find('a'))
print(text.rfind('a'))
print(text.index('a'))
print(text.rindex('a'))

text1='ABCabc123'
text2='123'
text3='ABC'
text4='abc'
print(text4.isalpha())
print(text4.isdigit())
print(text4.isalnum())
print(text4.isupper())
print(text4.islower())

text='ABCabc'
print(text.upper())
print(text.lower())
'''
m='1'
d='21'
y='2021'
print(m.zfill(2))
print(d.zfill(2))
print(y.zfill(4))
