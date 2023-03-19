import pandas as PD_Test

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

xlsx = PD_Test.read_excel('Test.xlsx', sheet_name='Diem')

print(xlsx)

