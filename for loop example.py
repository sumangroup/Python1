for x in range(0,10):
    print(x)

print('-'*50)

list1=[10,20,30]
for x in list1:
    print(x)
print('-'*50)

set1={10,20,30}
for x in set1:
    print(x)
print('-'*50)

tuple1=(10,20,30)
for x in tuple1:
    print(x)
print('-'*50)

dict1={
    "Name":"Raju Mane",
    "age":32
    }

for x in dict1:
    print(x,':',dict1[x])
print('-'*50)

for x,y in dict1.keys(),dict1.values():
    print(x,y)
print('-'*50)


for x in dict1.items():
    print(x)   
print('-'*50)

for x in dict1.values():
    print(x)   
print('-'*50)

