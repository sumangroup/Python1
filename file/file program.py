# write mode
myfile=open("hello.txt",'w')
print(myfile)
myfile.write("hello python\n")
myfile.write("hello raju\n")
myfile.write("hello mrunali\n")
myfile.close()

# read mode

myfile=open("hello.txt")
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

for line in open("hello.txt"):
    print(line,end='')
print()

with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

