s1={1,2,3,4,5}
s2={4,5,6,7,8}

print('s1',s1)
print('s2',s2)
union=s1 | s2
print('union',union)
intersection=s1 & s2
print('intersection',intersection)
difference=s1-s2
print('difference',difference)
difference=s2-s1
print('difference',difference)
symmetricdifference=s1 ^ s2
print('symmetricdifference',symmetricdifference)
