emp = {'eno':[1,2,3], 'ename':['A','B','C'],'esal':[10000,22000,30000]}
print("\n the employee data set is:")
print(emp)
print("-----")
print("\n the employee name are:",emp['ename'])
print("------")
print("the employee salaries are:")
print("------")
for i in emp['esal']:
    print(i)