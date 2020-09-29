# -*- coding: utf-8 -*-
from OracleProject.Employee import Employee
from OracleProject import OracleConnection as oc

def AddEmployee():
    e=Employee()
    e.empno=int(input('Enter employee number'))
    e.ename=input('Enter employee name')
    e.salary=float(input('Enter salary'))
    e.sex=input('Enter sex')
    e.dateofbirth=input('Enter date of birth')
    e.email=input('Enter email')
    rec=oc.ConnectionWithParameter(e,1)
    return rec

def UpdateEmployee():
    e=Employee()
    e.empno=int(input('Enter employee number'))
    e.ename=input('Enter employee name')
    e.salary=float(input('Enter salary'))
    e.sex=input('Enter gender')
    e.dateofbirth=input('Enter date of birth')
    e.email=input('Enter email')
    rec=oc.ConnectionWithParameter(e,2)
    return rec

def DeleteEmployee():
    e=Employee()
    e.empno=int(input('Enter employee number'))
    #e.ename=input('Enter employee name')
    #e.salary=float(input('Enter salary'))
    #e.sex=input('Enter gender')
    #e.dateofbirth=input('Enter date of birth')
    #e.email=input('Enter email')
    rec=oc.ConnectionWithParameter(e,3)
    return rec

def ShowAllEmployee():
    #e=Employee()
    rec=oc.ConnectionWithParameter(None,4)
    for r in rec:
        print(r)
    
    
    
    

