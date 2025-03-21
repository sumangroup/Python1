dict1={
    "Name":"Raju Mane",
    "age":32,
    "skills":["c","c++","java"]
    }

print('dict1',dict1,len(dict1))

dict2=dict()
print('dict2',dict2,len(dict2))
dict2["Name"]="Raju Mane"
dict2["Age"]=32
dict2["Skills"]=["c","c++","java"]
print('dict2',dict2,len(dict2))
dict2["Name"]="Mrunali"
print('dict2',dict2,len(dict2))
values1=dict2.get("Name")
print(values1)
values2=dict2.get("Skills")
print(values2)
item1=dict2.items()
print(item1)
key1=dict2.keys()
print(key1)
value1=dict2.values()
print(value1)
pop1=dict2.pop("Name")
print(pop1)
print('dict2',dict2,len(dict2))
dict2["Name"]="Mrunali"
print('dict2',dict2,len(dict2))
popitem=dict2.popitem()
print(popitem)

popitem=dict2.popitem()
print(popitem)

print('dict2',dict2,len(dict2))

dict2["Name"]='Mrunali Prasade'
dict2['skills']=["c","c++","java"]
print('dict2',dict2,len(dict2))
dict2.setdefault("Address")
print('dict2',dict2,len(dict2))
dict2.setdefault("contactno",12345678)
print('dict2',dict2,len(dict2))





    
