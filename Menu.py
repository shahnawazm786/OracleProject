# -*- coding: utf-8 -*-
from OracleProject.EmloyeeRespository import EmployeeRes as er
def Menu():
    print('1. Employee')
    print('2. Salary')
    print('3. Absent')
    print('4. Quit')
    opt=int(input('Enter options'))
    if opt==1:
        EmployeeMenu()
    elif opt==2:
        print('Salary opeations')
    elif opt==3:
        print('Absent Operations')
    elif opt==4:
        return
    else:
        print('Please valid options')
        Menu()
        

def EmployeeMenu():
    print('1. Add Employee')
    print('2. Update Employee')
    print('3. Delete Employee')
    print('4. All Employees')
    print('5. Quit')
    opt1=int(input('Enter options'))
    if opt1==1:
        er.AddEmployee()    
    elif opt1==2:
        er.UpdateEmployee()
    elif opt1==3:
        er.DeleteEmployee()
    elif opt1==4:
        er.ShowAllEmployee()
    elif opt1==5:
        return
    else:
        print('Please select valid options')
        EmployeeMenu()
