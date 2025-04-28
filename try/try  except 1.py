def process_data(data):
    if not isinstance(data,list):
        raise Exception("Input data must be a list.")
    if not data:
        raise Exception("Input list cannot be empty.")
    print("Data processed successfully:", data)


try:
    num=int(input("how many number you want to enter:"))
    i=0
    data=[]
    while i<num:
        value=int(input("enter value: "))
        data.append(value)
        i=i+1
    process_data(data)
except Exception as e:
    print(e)


    
