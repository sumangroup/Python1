import random
a=random.randint(1,10)
for i in range(0,3):

    w=int(input('Enter the number: '))
    if a==w:
        print('you won',a,w)
        break
    elif a<w:
        print('to high',a,w)
    else:
        print('to low',a,w)
