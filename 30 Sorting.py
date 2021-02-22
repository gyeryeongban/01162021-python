'''li=[2,4,6,8,10,1,3,5,7,9]

for i in range(len(li)):
    print(li)
    m_index=i
    for j in range(i,len(li)):
        if li[j]<li[m_index]:
            m_index=j
    li[i],li[m_index]=li[m_index],li[i]

#print(li)'''



li=[2,4,6,8,10,1,3,5,7,9]

for i in range(len(li)):
    print(li)
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]

#print(li)
