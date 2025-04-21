def f(*args):
    print(args)


f(1,2,310,20,30,4,5,0)

def f1(**args):
    print(args)

f1(name='Mrunali',rollno=101)

print()
def f2(a,*args,**kargs):
    print(a)
    print(args)
    print(kargs)

f2(1,20,30,40,50,name='Mrunali',rollno=101)

print("Calls: Unpacking argument")
def func1(a,b,c,d):
    print(a,b,c,d)

args=(10,20,30,40)
func1(*args)
print()
args = {'a': 1, 'b': 2, 'c': 3,'d':4}
func1(**args)













