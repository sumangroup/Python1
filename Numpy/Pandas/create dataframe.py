import pandas as pd
#excel
dt=pd.read_excel('Book1.xlsx')
print(dt)
print('-'*50)

dt1=pd.read_excel('Book1.xlsx',sheet_name='Sheet1', usecols='A:F', skiprows=1)
print(dt1)
print('-'*50)

# .csv file
dt2=pd.read_csv('test.csv')
print(dt2)
print('-'*50)


# python dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']

}
dt3 = pd.DataFrame(data)
print(dt3)
print('-'*50)

#python list of truple
data = [
    ('Alice', 25, 'New York'),
    ('Bob', 30, 'Los Angeles'),
    ('Charlie', 35, 'Chicago')
]
dt4=pd.DataFrame(data,columns=['Name', 'Age', 'City'])
print(dt4)

