import pandas as PD_Test

test_dict = {
            'P1' : [1.1,1.2,1.3,1.4],
            'P2' : [2.1,2.2,2.3,2.4],
            'P3' : [3.1,3.2,3.3,3.4]
             }

a = PD_Test.DataFrame(test_dict)


b = a['P1']
# print(b)
c = a.P1
# print(c)

d = a[['P1', 'P2']]
# print(d)

e = a.columns
# print(e)

f = a.iloc[[0]]
print(f)

g = a.iloc[[0,1]]
print(g)

