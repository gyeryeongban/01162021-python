'''li1=input('문자 입력').split()

li2=list(input('문자 입력'))

li3=[]

li3.append(int(input('숫자 입력')))
li3.append(int(input('숫자 입력')))
li3.append(int(input('숫자 입력')))

li4=list(map(int,input('숫자 입력').split()))

a=input('숫자 입력').split()
b=map(int,a)
c=list(b)'''

num=list(map(int,input('숫자 입력').split()))

num.sort()

#print('합:',sum(num))
#print('평균:',sum(num)/len(num))
print('최소값:',num[0])
print('최대값:',num[len(num)-1])
#print('중간값:',num[len(num)//2])
