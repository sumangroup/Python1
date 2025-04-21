def display(name,rollno,collname="SAKEC"):
    print('name',name)
    print('rollno',rollno)
    print('collname',collname)

display("Mrunali",101)
print()
display("Raju",101,'Kirti')

def f(a,b,c):
    print(a,b,c)

f(1,2,3)
f(c=3,b=2,a=1)
f(1,c=3,b=2)


def func(spam, eggs, toast=0, ham=0): # First 2 required
 print((spam, eggs, toast, ham))

func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)
func(4,0,toast=1)
