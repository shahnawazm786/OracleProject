# -*- coding: utf-8 -*-

class EmployeeSalary:
    def __init__(self):
        self.Empno=0
        self.Basic=0.0
        self.DA=0.0
        self.TA=0.0
        self.Phone=0.0
        self.HRA=0.0
        self.IT=0.0
        
    @property
    def empno(self):
        return self.Empno
    @empno.setter
    def empno(self,empno):
        self.Empno=empno
    
    @property
    def basic(self):
        return self.Basic
    @basic.setter
    def basic(self,bs):
        self.Basic=bs
        
    @property
    def da(self):
        return self.DA
    @da.setter
    def da(self,da):
        self.DA=da
        