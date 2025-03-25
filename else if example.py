a=int(input('Enter the number a: '))
b=int(input('Enter the number b: '))
c=int(input('Enter the number c: '))

if a>b and a>c:
    print('a is greater')
elif b>a and b>c:
    print('b is greater')
elif c>a and c>b:
    print('c is greater')
elif a==b==c:
    print("all are equal")
