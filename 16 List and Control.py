li=[7,5,4,1,9]

'''for i in range(5):
    li.append(int(input('문자 입력:')))


for i in range(len(li)):
    print(li[i])

for i in li:
    print(i)


for i in range(len(li)):
    if i%2==0:
        print(li[i])

print()

for i in li:
    if i%2==0:
        print(i)'''


li=list(input('문자 입력:'))

up=[]
low=[]

for i in li:
    if i.isupper():
        up.append(i)
    elif i.islower():
        low.append(i)

print(up)
print(low)
