import datetime
print("\t\t\tToday's date is:",datetime.datetime.now())
import mysql.connector as h
from tabulate import tabulate
mydb=h.connect(host='localhost',user='root',password='root')
mycursor=mydb.cursor()

def display(x):
  z=int(input('Enter Number Of the Table(i.e 1st,2nd..):'))
  sql="create database if not exists %s"%("Display")
  mycursor.execute(sql)
  mycursor.execute("Use Display")
  fun="Create table if not exists menu \
  (Number int, \
  MAIN_MENU varchar(20) primary key)"
  mycursor.execute(fun)
  rec=(z,x)
  query="insert into menu values(%s,%s)"
  mycursor.execute(query,rec)
  mydb.commit()
  print('Table added')
                
def table():
  db1=input('Please Enter the name of your database:')
  TableName=input("Enter the Name of the Table to be created:")
  sql="create database if not exists %s"%(db1)
  mycursor.execute(sql)
  mycursor.execute('Use '+db1)
  return TableName

def main_menu():
  sql="create database if not exists %s"%("MAIN_MENU")
  mycursor.execute(sql)
  mycursor.execute("Use MAIN_MENU")
  fun="Create table if not exists "+hi+" \
  (SrNo int not null primary key,\
  Items varchar(30),\
  price float)"
  mycursor.execute(fun)
  print('-'*100)
  print('Table creation Successfully in MAIN_MENU database')
  print('-'*100)
  sql="create database if not exists %s"%("Display")
  
while True:
  print('--------------|')
  print('1-->CUSTOMER  |')
  print('2-->ADMIN     |')
  print('3-->Exit      |')
  print('--------------|')
  x=int(input('Enter your choice here:)--->'))
  if x==2:
      kkr=input('Enter the Password:')
      if kkr=='DPS':
        print('\n\n')
        print('-'*40,'WELCOME BACK ADMIN','-'*40)
        while True:
          print('\n')
          print('*'*100)
          print('\t\t\t\tMAIN MENU')
          print('*'*100)
          print('\t\t\t\t1.  Adding Employee Records')
          print('\t\t\t\t2.  Adding Items in Main Menu')
          print('\t\t\t\t3.  For Displaying Records of All the Employees')
          print('\t\t\t\t4.  For Displaying Records of a Particular Employees')
          print('\t\t\t\t5.  For Displaying All Records of MAIN MENU')
          print('\t\t\t\t6.  For Deleting Records Of All the Employeee')
          print('\t\t\t\t7.  For Deleting a Records of a Particular Employee')
          print('\t\t\t\t8.  For Modifying Employee Record')
          print('\t\t\t\t0.  For Exit')
          choice=int(input('Enter your Choice:'))
          if choice==1:
            TableName=table()
            query="Create table if not exists "+TableName+" \
            (BatchNumber int primary key,\
            First_NAME varchar(20) not null,\
            Last_NAME varchar(20) not null,\
            JOB varchar(20) not null,\
            DateOfJoining date not null,\
            BasicSalary int not null)"
            print("\t\t\tTable "+TableName+" created successfully.....")
            mycursor.execute(query)
            print('-'*100)
            try:
              print('\t\t\tEnter Employee Information')
              print('\t\t\tAll Informations are Mandotory')
              print('-'*100)
              o=int(input('How Many Records Do You Want To Insert:'))
              for i in range(0,o):
                mempno=int(input('Enter BatchNumber:'))
                mname =input('Enter First Name:')
                mname2 =input('Enter Last Name:')
                mjob=input('Enter Job:')
                mdob=input('Enter the Date of Joining:')
                mbasic=float(input('Enter BasicSalary:'))
                rec=(mempno,mname,mname2,mjob,mdob,mbasic)
                query="insert into "+TableName+" values(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query,rec)
                mydb.commit()
                print('-'*100)  
                print('***HURRAY! Record Added Successfully***')
            except Exception as e:
              print('Oops! Something Went Wrong[:(]',e)  
          elif choice==2:
            hi=input('Enter the Table Name:')
            display(hi)
            main_menu()
            while True:
              SrNo=int(input('Enter the SrNo:'))
              Soup=input('Enter the Name of the Item:')
              Price=int(input('Enter the Price:'))
              print('-'*20,'Table name is',hi,'-'*20)
              rec=(SrNo,Soup,Price)
              query="insert into "+hi+" values(%s,%s,%s)"
              mydb.cursor().execute(query,rec)
              mydb.commit()
              print('Record Added Successfully!!!')
              x=input('Do you want to add more Records(y/n):')
              if x=='y':
                  continue
              else:
                  break
          elif choice==3:
            try:
                x=input('Enter the Database:')
                y=input('Enter the Table Name:')
                mycursor.execute("Use "+x)
                query="select * from "+y
                mycursor.execute(query)
                print(tabulate(mycursor,headers=['BatchNumber','First_NAME','Last_NAME','JOB','DateOfJoining','BasicSalary'],tablefmt='psql'))
            except Exception as e:
                print('Something Went Wrong!!!',e)
          elif choice==4:
            x1=input('Enter the Database:')
            y=input('Enter the Table Name:')
            mycursor.execute("Use "+x1)
            x=input('PLease Enter the BatchNumber HERE:')
            query="select * from "+y+" where BatchNumber="+x
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['BatchNumber','First_NAME','Last_NAME','JOB','DateOfJoining','BasicSalary',],tablefmt='psql'))
            c=mycursor.rowcount
            if c==-1:
              print('Nothing To Display')
          elif choice==5:
            mycursor.execute("Use MAIN_MENU")
            TableName=input('Enter the TableName:')
            query="select * from "+TableName
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['SrNo','Item Name','Price'],tablefmt='psql'))
          elif choice==6:
            try:
              x=input('Enter the Database:')
              y2=input('Enter the Table Name:')
              mycursor.execute("Use "+x)
              y=input('Do You Want to Delete All The Records(y/n):')
              if y=='y':
                mycursor.execute("delete from "+y2)
                mydb.commit()
                print('All Records are Deleted!!!')
            except Exception as e:
              print('Something Went Wrong',e)
          elif choice==7:
            try:
              x=input('Enter the Database:')
              y2=input('Enter the Table Name:')
              mycursor.execute("Use "+x)
              y=input('Enter BatchNumber:')
              query="delete from "+y2+" where BatchNumber= "+y
              mycursor.execute(query)
              mydb.commit()
              c=mycursor.rowcount
              if c>0:
                print('Deletion Done')
              else:
                print('BatchNumber',y,'not Found')
            except Exception as e:
              print('Something Went Wrong',e)
          elif choice==8:
            try:
              x=input('Enter the Database:')
              y=input('Enter the Table Name:')
              mycursor.execute("Use "+x) 
              SrNo=input("Enter BatchNumber to Modify:")
              query="select * from  "+y+" where BatchNumber= "+SrNo
              mycursor.execute(query)
              myrecord=mycursor.fetchone()
              c=mycursor.rowcount
              if c==-1:
                print("SrNo "+prno+" does not exist")
              else:
                tBN=myrecord[0]
                tname=myrecord[1]
                tname2=myrecord[2]
                tjob=myrecord[3]
                tDOJ=myrecord[4]
                tBS=myrecord[5]
                print("BatchNumber            : ",myrecord[0])
                print("First_NAME             : ",myrecord[1])
                print("Last_NAME              : ",myrecord[2])
                print("JOB                    : ",myrecord[3])
                print("DateOfJoining          : ",myrecord[4])
                print("BasicSalary            : ",myrecord[5])
                print("-"*25)
                print("Type New value if you want to modify or press enter for no change")
                x=input("Enter new First_Name or press enter for no change")
                if len(x)>0:
                  tname=x
                x=input("Enter new Last_Name or press enter for no change")
                if len(x)>0:
                  tname2=x
                x=input("Enter new Job name or press enter for no change")
                if len(x)>0:
                  tjob=x
                x=input("Enter new Date of Joining or press enter for no change")
                if len(x)>0:
                  tDOJ=x
                x=input("Enter new BasicSalary or press enter for no change")
                if len(x)>0:
                  tBS=int(x)
                query='update '+y+' set  NAME=%s,Last_NAME=%s,JOB=%s,DateOfJoining=%s,BasicSalary=%s                    where BatchNumber=%s'
                rec=(tname,tname2,tjob,tDOJ,tBS,SrNo)
                mycursor.execute(query,rec)
                mydb.commit()
                print("Record modified")
            except Exception as e:
              print("error in modifying",e)
          elif choice==0:
            break

  if x==1:
    prlst=[]
    print('-'*100)
    print(25*' ','WELCOME to PHOENIX Restaurant!!!',25*' ')
    print(25*' ','Good Food and Good Vibes',25*' ')
    print(25*' ','Satisfy your Snack Attack',25*' ')
    print('-'*100)
    print('NOTE--->>Please  Order Everything, So not to Squander your Time')
    print('-'*100)
    print('WE HAVE VARIETIES AS FOLLOWS')
    while True:
      mycursor.execute("Use Display") 
      y="select * from menu"
      mycursor.execute(y)
      print(tabulate(mycursor,headers=['SrNo','Menu'],tablefmt='fancy_grid'))
      cus=input('Enter the Name:')
      mycursor.execute("use MAIN_MENU")
      mycursor.execute("select * from "+cus)
      print('-'*100)
      print(tabulate(mycursor,headers=['SrNo','Item_Name','Price'],tablefmt='fancy_grid'))
      mycursor.execute("select * from "+cus)
      myrecord=mycursor.fetchone()
      c=mycursor.rowcount
      enter=int(input('Enter the SrNo Here:'))
      if c==-1:
        print('Product Number',enter,'does not Exist!!!')
        break
      elif enter==0:
        break
      else:
        qty=input('Enter the Quantity:')
        price=int(qty)*myrecord[2]
        lst=[myrecord[1],qty,price]
        prlst.append(lst)
        x=input('Do you want to buy more(y/n):')
        print('-'*100)
        if x=='y':
          continue
        else:
          break
    if len(prlst)>0:
      tamount=0
      for i in prlst:
        print('Product Name:',i[0],' '*8,'Quantity:',i[1],' '*8,'Price:',i[2])
        tamount+=int(i[2])
      print()
      print()
      print()
      print('Total Amount Payable             :',tamount)
      print('-'*100)
      print('ENJOY YOUR DINNER')
      print('VISIT AGAIN')
      print('BYE')
      break
    else:
      print('No Product Sold') 
  if x==3:
    break

