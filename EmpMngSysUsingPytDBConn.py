#Employee Management System using Python Database Connection
import cx_Oracle

menu="""+--------------------------------------------------+
		Employee Information System
+--------------------------------------------------+
|		1. New Employee			|
|		2. Update Employee		|
|		3. Remove Employee		|
|		4. View Single Employee		|
|		5. View All Employee		|
|		6. Exit				|
+--------------------------------------------------+"""

update_menu="""\tWhat want to update?
+--------------------------------------------------+
|		1. Name of Employee          |
|		2. Salary of Employee        |
|		3. Job of Employee           |
|		4. Exit                      |
+--------------------------------------------------+"""

def newemp():
    while(True):
        try:
            con = cx_Oracle.connect("chamat/pranay1998@localhost/xe")
            cur = con.cursor()
            empno=int(input("Enter Employee No.: "))
            ename=input("Enter Name of Employee: ")
            sal=float(input("Enter Salary of Employee: "))
            job=input("Enter Job of Employee: ")
            cur.execute("insert into employees values(%d,'%s', %f, '%s')" %(empno, ename, sal, job))
            con.commit()
            rc = cur.rowcount
            if rc == 0:
                print("New Employee record saved unsuccessfully")
            else:
                print("{} Employee record saved successfully".format(cur.rowcount))
            ch=input("Do you want add another employee record?(yes/no):")
            if (ch.lower()=="no"):
                break
        except cx_Oracle.DatabaseError as db:
            print("Problem in Datebase:",db)
        except ValueError:
            print("Dont enter alphnums, symbol, strs in empno and sal")

def updateemp():
    while (True):
        try:
            con = cx_Oracle.connect("chamat/pranay1998@localhost/xe")
            cur = con.cursor()
            print(update_menu)
            chh=int(input("Enter your choice : "))
            if (chh==1):
                empno=int(input("Enter Employee No.: "))
                ename=input("Enter Name of Employee: ")
                cur.execute("update employees set ename='%s' where eno=%d" %(ename, empno))
            elif chh==2:
                empno=int(input("Enter Employee No.: "))
                sal=float(input("Enter Salary of Employee: "))
                cur.execute("update employees set sal=%f where eno=%d" % (sal, empno))
            elif chh==3:
                empno=int(input("Enter Employee No.: "))
                job=input("Enter Job of Employee: ")
                cur.execute("update employees set job='%s' where eno=%d" % (job, empno))
            elif chh==4:
                break
            else:
                print("select appropriate option")
            con.commit()
            rc=cur.rowcount
            if rc==0:
                print("Employee record updated unsuccessfully")
            else:
                print("{} Employee record updated successfully".format(cur.rowcount))
        except cx_Oracle.DatabaseError as db:
            print("Problem in Datebase:", db)
        except ValueError:
            print("Dont enter alphnums, symbol, strs in empno and sal")


def removeemp():
    while (True):
        try:
            con = cx_Oracle.connect("chamat/pranay1998@localhost/xe")
            cur = con.cursor()
            print("To Remove Employee")
            empno = int(input("Enter Employee No.: "))
            cur.execute("delete from employees where eno=%d" %empno)
            con.commit()
            rc = cur.rowcount
            if rc == 0:
                print("Employee record deleted unsuccessfully")
            else:
                print("{} Employee record deleted successfully".format(cur.rowcount))
            ch = input("Do you want remove another employee record?(yes/no):")
            if (ch.lower() == "no"):
                break
        except cx_Oracle.DatabaseError as db:
            print("Problem in Datebase:", db)
        except ValueError:
            print("Dont enter alphnums, symbol, strs in empno")


def viewemp():
    try:
        con = cx_Oracle.connect("chamat/pranay1998@localhost/xe")
        cur = con.cursor()
        cur.execute("select * from employees order by eno asc")
        print("+--------------------------------------------------+")
        vw=cur.description
        for v in vw:
           print(v[0],end="\t")
        print()
        print("+--------------------------------------------------+")
        rec=cur.fetchall()
        for record in rec:
            for val in record:
                print(val,end="\t")
            print()
        print("+--------------------------------------------------+")
        print("{} Employee record selected".format(cur.rowcount))
    except cx_Oracle.DatabaseError as db:
        print("Problem in Datebase:", db)


def viewoneemp():
    try:
        con = cx_Oracle.connect("chamat/pranay1998@localhost/xe")
        cur = con.cursor()
        eno=int(input("Enter Employee No. : "))
        cur.execute("select * from employees where eno=%d" %eno)
        print("+--------------------------------------------------+")
        vw=cur.description
        for v in vw:
           print(v[0],end="\t")
        print()
        print("+--------------------------------------------------+")
        rec=cur.fetchall()
        for record in rec:
            for val in record:
                print(val,end="\t")
            print()
        print("+--------------------------------------------------+")
        print("{} Employee record selected".format(cur.rowcount))
    except cx_Oracle.DatabaseError as db:
        print("Problem in Datebase:", db)

#mainprogram

import cx_Oracle
while(True):
    print(menu)
    try:
        choice=int(input("Enter your Choice : "))
        print("+--------------------------------------------------+")
        match(choice):
            case 1:
                newemp()
            case 2:
                updateemp()
            case 3:
                removeemp()
            case 4:
                viewoneemp()
            case 5:
                viewemp()
            case 6:
                print("Thanks for using this Application")
                break
            case _:
                print("Select appropriate index no, Enter no. between 1 to 6 only")
    except ValueError:
        print("Dont enter alphnum, symbol and strs, enter index no. only")



