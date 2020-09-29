# -*- coding: utf-8 -*-

import cx_Oracle as cx
l=[]
def ConnectionWithParameter(emp,operations):
   if operations==1:
       try:
           cn=cx.connect('scott/tiger@localhost:1521/orcl')
           cur=cn.cursor()
           sql='''
           insert into tbl_employee 
           (Empno,Ename,Salary,DOB,Gender,Email)
           values(:empno,:ename,:salary,:dateofbirth,:sex,:email)
           '''
           para=[emp.empno,emp.ename,emp.salary,emp.dateofbirth,emp.sex,emp.email]
           cur.execute(sql,para)
       
       except:
            print('Error')
       else:
            cn.commit()
            cn.close()
            print('Record inserted successful')
   elif operations==2:
       try:
           cn=cx.connect('scott/tiger@localhost:1521/orcl')
           cur=cn.cursor()
           sql='''
           update tbl_employee
           set Ename=:ename,
           Salary=:salary,
           DOB=:dateofbirth,
           Gender=:sex,
           Email=:email
           where Empno=:empno
           '''
           para={'ename':emp.ename,'salary':emp.salary,'dateofbirth':emp.dateofbirth,'sex':emp.sex,'email':emp.email,'empno':emp.empno}
           cur.execute(sql,para)
       except:
            print('Error in updating')
       else:
            cn.commit()
            cn.close()
            print('Record updated')
   elif operations==3:
       try:
           cn=cx.connect('scott/tiger@localhost:1521/orcl')
           cur=cn.cursor()
           sql='''
           Delete from tbl_employee
           where Empno=:empno
           '''
           para=[emp.empno]
           cur.execute(sql,para)
       except:
            print('Error in Deleting')
       else:
            cn.commit()
            cn.close()
            print('Record Deleted')
   elif operations==4:
       try:
           cn=cx.connect('scott/tiger@localhost:1521/orcl')
           cur=cn.cursor()
           sql='Select * from tbl_employee'
           records=cur.execute(sql)
           return records
       except:
            print('Error in fetched')
       else:
            
            cn.close()
            print('Record Fetched')
   else:
        print('No operationed performed')
        
        
    
    