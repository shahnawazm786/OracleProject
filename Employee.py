# -*- coding: utf-8 -*-
# Model
class Employee:
    def __init__(self):
        self.Empno=0
        self.Ename=None
        self.BasicSalary=0.0
        self.Gender=None
        self.DOB=None
        self.Email=None
    
    @property
    def empno(self):
        return self.Empno
    @empno.setter
    def empno(self,eno):
        self.Empno=eno
    
    @property
    def ename(self):
        return self.Ename
    @ename.setter
    def ename(self,enm):
        self.Ename=enm
    
    @property
    def salary(self):
        return self.BasicSalary
    @salary.setter
    def salary(self,bs):
        self.BasicSalary=bs
    
    @property
    def sex(self):
        return self.Gender
    @sex.setter
    def sex(self,gen):
        self.Gender=gen
    
    
    @property
    def dateofbirth(self):
        return self.DOB
    @dateofbirth.setter
    def dateofbirth(self,db):
        self.DOB=db
        
    @property
    def email(self):
        return self.Email
    @email.setter
    def email(self,eml):
        self.Email=eml
    
    
    