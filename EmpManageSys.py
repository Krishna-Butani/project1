# Employee Management System Using Python – copyassignment.com
from os import system
import re

import mysql.connector
#making Connection
conn  = mysql.connector.connect(host = "localhost",
                                user = "root",
                                password = "",
                                database = "employee")
mycursor = conn.cursor()#allows row-by-row processing of the result sets.
#mycursor.execute("CREATE DATABASE employee")
#mycursor.execute("CREATE TABLE empdata (Id INT (11) PRIMARY KEY , Name VARCHAR(2000), Email_Id TEXT(2000),Phone_no BIGINT(11), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(20))")

# make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")

#Function to add_employee
def Add_Employ():
    print("{:>60}".format("--->> Add Employee Record <<---"))
    Id = input("Enter Employee Id: ")
    #checking If Employee Id is Exit or Not
    if (check_employee(Id) == True):
        print("Employee Id Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
        
    Name = input("Enter Employee Name: ")
    #cheaking If Employee Name is Exit Or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Aldready Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ
        
    Email_Id = input("Enter Employee Email Id: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email..!!")
    else:
        print("Invalid Email..!!")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    
    Phone_no =input("Enter Employee Phone No.: ")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number!!")
    else:
        print("Invalid Phone Number!!")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary:")
    
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    #Inserting Employee Details in
    #The Employee(empdata) Table
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = conn.cursor()
    
    #Executing the sql Query
    c.execute(sql, data)
    
    # Commit() method to make changes in the table
    conn.commit()
    print("Sucessfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()
    
        
#Function To Check if Employee With given Name Exist or not
def check_employee_name(employee_name):
    #query to select all Rows from 
    #employee(empdata) table
    sql = 'select * from empdata where Name=%s'
    
    #making cursor buffered to make
    # rowcount method work properly
    c = conn.cursor(buffered=True)
    data = (employee_name,)
    
    #Execute the sql query 
    c.execute(sql, data)
    
    #rowcount method to find number of row with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
    
#Function To Check id Employee With given Td Exist or not
def check_employee(employee_id):
    #query to select all Rows from employee(empdata) table
    sql = 'select * from empdata where Id=%s'
    
    #making cursor buffered to make rowcount method work properly
    c = conn.cursor(buffered=True)
    data = (employee_id,)
    
    #Execute the sql query
    c.execute(sql,data)
    
    #rowcount method to find number of row with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
    
    
# Function to Display_Emp
def Display_Employ():
    print("{:>60}".format("--->> Display Employee Record <<---"))
    #query to select all rows from Employee (empdata) Table
    sql = 'select * from empdata'
    c = conn.cursor()
    
    #Executing the sql query
    c.execute(sql)
    
    #Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee id: ",i[0])
        print("Employee Name: ",i[1])
        print("Employee Email Id: ",i[2])
        print("Employee Phone No: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee Post: ",i[5])
        print("Employee Salary: ",i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()
    
#Funtion to Update_Employee
def Update_Employ():
    print("{:>60}".format("--->> Update Employee Record <<---\n"))
    Id = input("Enter Employee Id: ")
    # Checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exist \nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id = input("Enter Employee Email ID: ")
        if(re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = eval(input("Press Any Key To Continue.."))
            Update_Employ()
        Phone_no = input("Enter Employee Phone No.: ")
        if(Pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number") 
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Address = input("Enter Employee Address: ")
        #Updating Employee details in empdata Table
        sql = 'UPDATE empdata set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = conn.cursor()
        
        #Executing the sql query
        c.execute(sql, data)
        
        #commit() method to make changes in the table
        conn.commit()
        print("Updated Emplpyee Record")
        press = input("Press ANy Key To Continue..")
        menu()
        
        
#Function to Promote_Employ
def Promote_Employ():
    print("{:>60}".format("--->> Promote Employee Record <<---"))
    Id = input("Enter Employee Id: ")
    # cheking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exist \nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount = int(input("Enter Increase Salary: "))
        #query to fetch salary of Employee with given data
        sql = 'select Salary from empdata where Id= %s'
        data = (Id,)
        c = conn.cursor()
        
        #executing the sql query
        c.execute(sql, data)
                
        #fetching salary of Employee with given Id
        r = c.fetchone()
        t = r[0] + Amount
        
        #query to update salary of Employee with given id 
        sql = 'update empdata set Salary = %s where Id  = %s'
        d = (t, Id)
        
        #exectuting the sql query
        c.execute(sql, d)
        
        #ommit() method to make changes in the table
        conn.commit()
        print("Employee Promoted")
        press = input("Press Any Key To Continue..")
        menu() 
        
        
#Funtion to Remove_Employee
def Remove_Employ():
    print("{:>60}".format("--->> Remove Employee Record <<---\n"))
    Id = input("Enter Employee Id: ")
    #cheking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("EMployee Record Not exists \nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        #query to delete Employee from empdata table
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = conn.cursor()
        
        #executing the sql query
        c.execute(sql, data)
        
        #commit() method to make changes in the empdata table
        conn.commit()
        print("Employee Removed")
        press = input("Press ANy Key To Continue..")
        menu()
        
        
#Function to Search_Employ
def Search_Employ():
    print("{:>60}".format("--->> Search Employee Record <<---\n"))
    Id = input("Enter Employee Id: ")
    #checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        #query to search Employee from empdata table
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = conn.cursor()
        
        #executing the sql query
        c.execute(sql, data)
        
        #fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any Key To Continue..")
        menu() 
        
        
#Menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("--->> Employee Management System <<---"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee Redord \n2. Display Employee Record \n3. Update Employee Record \n4. Promote Employee Record \n5. Remove Employee Record \n6. Search Employee Record \n7. Exit\n")
    print("{:>60}".format("--->> Choice Options: [1 to 7] <<---"))
    
    ch = int(input("Enter your Choice: "))
    match(ch):
        case 1:
            system("cls")
            Add_Employ()
        
        case 2:
            system("cls")
            Display_Employ()
        
        case 3:
            system("cls")
            Update_Employ()
                
        case 4:
            system("cls")
            Promote_Employ()
        
        case 5:
            system("cls")
            Remove_Employ()
        
        case 6:
            system("cls")
            Search_Employ()
        
        case 7:
            print("{:>60}7".format("Have a Nice Day!!.."))
            system("cls")
            exit(0)
            
        case _:
            print("Invalid Choice!!..")
            press = input("Press Any Key To Continue..")
            menu()
            
#Calling menu function
menu() 




#C:\Users\Home\Desktop\Krishna\python\Python Project\EmpManageSys.py