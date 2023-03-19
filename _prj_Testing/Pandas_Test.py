import pandas as PD_Test
import os
test_dict = {
            'P1' : ['P1.1', 'P1.2', 'P1.3', 'P1.4'],
            'P2' : ['P2.1', 'P2.2', 'P2.3', 'P2.4'],
            'P3' : ['P3.1', 'P3.2', 'P3.3', 'P3.4']
             }

a = PD_Test.DataFrame(test_dict)
# print(a)


b = a['P1']
# print(b)
c = a.P1
# print(c)

d = a[['P1', 'P2']]
# print(d)

e = a.columns
# print(e)

# ANCHOR - Index LOC:
f = a.iloc[[0]] #lấy hàng (line of code)
# print(f)

g = a.iloc[[0,1],[0,2]]# lấy nhiều hàng (line of code) , cột phải là index
# print(g)

h = a.iloc[0,1] #[hàng, cột]
# print(h)

# ANCHOR - LOC:
i = a.loc[[0,1],['P1','P2']] #[hàng, cột], cột phải là tên keys
# print(i)


# ANCHOR - xlsx:
cur_dir = os.getcwd()
# print(cur_dir)
xlsx = PD_Test.read_excel('C:\Test.xlsx', sheet_name='Diem')
# print(xlsx)
# print(xlsx.shape)
# print(xlsx.columns)
# print(xlsx.columns.ravel()) #set all column name to a list
# print(xlsx['Long'].tolist()) #set a specific column to a list
# print(xlsx['Long'].value_counts())
# print(xlsx.loc[[0,2],'Diễm'])

'''We can specify the column names to be read from the excel file. It’s useful when you are interested in only a few of the columns of the excel sheet'''
xlsx_specific = PD_Test.read_excel('C:\Test.xlsx', sheet_name='Diem', usecols=['Nhân', 'Diễm', 'Mai'])
# print(xlsx_specific)

'''If the excel sheet doesn’t have any header row, pass the header parameter value as None.'''
xlsx_without_header = PD_Test.read_excel('C:\Test.xlsx', sheet_name='Diem', header=None)
# print(xlsx_without_header)

'''The DataFrame object has various utility methods to convert the tabular data into Dict, CSV, or JSON format.'''
xlsx_to_dict = PD_Test.read_excel('C:\Test.xlsx', sheet_name='Diem', usecols=['Nhân', 'Diễm'])
print('Excel Sheet to Dict:', xlsx_to_dict.to_dict(orient='record'))
print('Excel Sheet to JSON:', xlsx_to_dict.to_json(orient='records'))
print('Excel Sheet to CSV:\n', xlsx_to_dict.to_csv(index=False))

