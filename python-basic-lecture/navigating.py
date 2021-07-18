'''li=[2,4,6,8,10,1,3,5,7,9]
n=int(input('1~10:'))

for i in range(len(li)):
    if li[i]==n:
        print(i)
        break'''



li=[2,4,6,8,10,12,14,16,18]
n=int(input('2,4,6,8,10,12,14,16,18: '))

s_index=0
e_index=len(li)-1

while s_index<=e_index:
    m_index=(s_index+e_index)//2
    print(s_index,e_index,m_index)
    if n<li[m_index]:
        e_index=m_index-1
    elif n>li[m_index]:
        s_index=m_index+1
    else:
        print(m_index)
        break
