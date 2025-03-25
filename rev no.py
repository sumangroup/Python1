num=int(input("Enter the number: "))
num1=num
res=0

while num!=0:
    r=num%10
    res=res*10+r
    num=num//10

print('res',res)
if num1==res:
    print('palindrome')
else:
    print('not palindrome')
