import sys

coworkers = ['Thomas', 'Anne', 'David', 'Ika', 'Jessica']
def showAllEmployees():
    '''Displays a list of all employees in the terminal'''
    for employee in range(0,len(coworkers)):
        print("[{}]: {}".format(employee, coworkers[employee]))

showAllEmployees()

print("Coworker at [2] index (third coworker): {}".format(coworkers[2]))

del coworkers[2]
print("Deleted employee [2]")
showAllEmployees()

del coworkers[0:2]
print("Deleted employees [0:2]")
showAllEmployees()

del coworkers[:]
print("Deleted coworkers [:]")
showAllEmployees();
print("0------------------------0")

firstName = ["Rob","Siri","Joanne","Gayan","Raya","Prathiba"]
def sort(vals):
    pass1, pass2 = 0, 0
    while pass1 < len(vals):
        while pass2 < len(vals):
            if(vals[pass1] > vals[pass2]):
                
            pass2 += 1
        pass1 += 1
        pass2 = 0
    return vals
sort(firstName)
print(firstName)
print(firstName.sort())