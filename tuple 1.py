t1=(
    10,
    20,
    30,
    ("Mrunali",'Vaidehi','Raju'),
    {
        'name':'Raju mane',
        'age':32,
        'skills':['c','c++','java']
        }
    ,
    [56.23,89.56,56.10,80,70,90,40,60]
    )
print('t1',t1,len(t1))
print(t1[3][1])
print(t1[4]['skills'][:2])
print(t1[5][1:5])
print(t1[1:5])
print('-'*50)

t2=(10,20,30)
t3="Raju","Vaidehi","Mrunali"
t4=t2+t3
print('t4',t4,len(t4))
t5=t2*3
print('t5',t5,len(t5))


t6=(50,60,80,70,90,50,56,23,90)
print('t6',t6,len(t6))
count1=t6.count(50)
print('count1',count1)

index1=t6.index(90,5)
print('index1',index1)


