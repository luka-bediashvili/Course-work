import csv
import sqlite3
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import numpy as np
import hashlib
import time
import sys

class start_up():
    def login():
        print('please enter user ID and password')
        with open('User_ID_Passwords.csv', 'r') as csvfile:
            login = csv.DictReader(csvfile, fieldnames=['user_ID', 'Passwords', 'name'], delimiter='\t')
            accept = False
            while accept == False:
                User_ID = input('User ID : ')
                password = input('password: ')
                encoded_password = password.encode('utf-8')
                password = hashlib.md5(encoded_password).hexdigest()
                for row in login:
                    Username_check=row['user_ID']
                    Password_check=row['Passwords']
                    welcome_name=row['name']
                    if (Username_check == User_ID and Password_check == password):
                        print('Accepted')
                        print('All pending orders')
                        system.pending()
                        start_up.name=welcome_name
                        start_up.main_menu()
                        accept = True
                    #start_up.login()
                

    def main_menu():
        print('')
        print('Welcome',start_up.name,'to Ucl academys leger')
        print('please choose one of the following options')
        print('To Open overview enter 1')
        print('To open user database enter 2')
        print('To open orders enter 3')
        print('To open graphs enter 4')
        print('To exit enter 0')
        try:
            option = int(input())
            if option == 1:
                system.overview()
            elif option == 2:
                system.user_data()
            elif option == 3:
                system.orders()
            elif option == 4:
                system.graphs()
            elif option == 0:
                print('good bye')
            else:
                print('invaild option')
                system.main_menu()
        except ValueError:
            print('ValueError')
            system.main_menu()
class system(start_up):
    def overview():
        print('please choose one of the following options')
        print('To search for data enter 1')
        print('To open total overview enter 2')
        print('To open todays overview enter 3')
        print('To add new data enter 4')
        print('for a deparment breakdown enter 5')
        print('to edit data enter 6')
        print('to return to main menu enter 7')
        option = int(input())
        while option > 7 or option == 0:
            print('value too high')
            overview()
            break
        try:
            if option == 1:
                system.search()
            elif option == 2:
                system.total_overview()
            elif option == 3:
                system.today_overview()
            elif option == 4:
                system.new_data()
            elif option == 5:
                system.department()
            elif option == 5:
                system.department()
            elif option == 7:
                system.main_menu()
            else:
                print('invaild option')
                system.main_menu()
        except ValueError:
            print('ValueError')
            overview()

    def today_overview():
        date = dt.datetime.now()
        print(date)
        date= date.strftime("%d/%m/%Y")
        print(date)
        with sqlite3.connect('The_database.db') as db2:
            find = db2.cursor()
            find.execute('select * from Totaloverview where Dateandtime=?',(date,))
            data=find.fetchall()
        for x in range(0,len(data)):
            print(data[x])
        #system.main_menu()
    def total_overview():
        i=0
        with sqlite3.connect('The_database.db') as db2:
            find = db2.cursor()
            find.execute('select * from Totaloverview')
            data=find.fetchall()
            while i!=(len(data)):
                print(data[i])
                i+=1
        system.main_menu()
    def search():
        print('please enter the following data enter 0 if not required ')
        try:
            Date = input('date in the form DD/MM/YYYY ')
        except ValueError:
            print('ValueError')
            system.search()
        try:
            Case_No = int(input('Case number '))
        except ValueError:
            print('ValueError')
            system.search()
        try:
            User_iD = int(input('User ID '))
        except ValueError:
            print('ValueError')
            system.search()
        department_ID = input('department ID ')
        try:
            min=int(input('price range min'))
            max = int(input('price range max'))
        except ValueError:
            print('ValueError')
            system.search()
        print(Date)
        print(Case_No)
        print(User_iD)
        print(department_ID)
        while Date=='' and Case_No=='' and User_iD=='' and department_ID=='' :
            print('no option detected')
            search()
            break
        if Date=='':
            print('No Date')
        else:
            with sqlite3.connect('The_database.db') as db2:
                find = db2.cursor()
                find.execute('select * from Totaloverview where Dateandtime=? ',(Date,))
                found = find.fetchall()
            print('Date')
            for x in range(0,(len(found))):
                print(found[x])
        if Case_No=='0':
            print('No Case number')
        else:
            with sqlite3.connect('The_database.db') as db2:
                find = db2.cursor()
                find.execute('select * from Totaloverview where "CaseNo."=? ',(Case_No,))
                found = find.fetchall()
            print('Case number')
            for x in range(0,(len(found))):
                print(found[x])
        if User_iD=='':
            print('No User ID')
        else:
            with sqlite3.connect('The_database.db') as db2:
                find = db2.cursor()
                find.execute('select * from Totaloverview where UseriD=? ',(User_iD,))
                found = find.fetchall()
            print('User ID')
            for x in range(0,(len(found))):
                print(found[x])

        if department_ID=='0':
            print('No Department given')
        else:
            with sqlite3.connect('The_database.db') as db2:
                find = db2.cursor()
                find.execute('select * from Totaloverview where departmentID=? ',(department_ID,))
                found = find.fetchall()
            print('Department')
            for x in range(0,(len(found))):
                print(found[x])
        if min==0 and max==0:
            print('No min max range')
        else:
            with sqlite3.connect('The_database.db') as db2:
                find = db2.cursor()
                find.execute('select * from Totaloverview where costofitem>? AND costofitem<? ',(min,max))
                found = find.fetchall()
                for x in range(0, (len(found))):
                    print(found[x])
        system.main_menu()
    def new_data():
        print('please enter the following data leave blank if not needed')
        try:
            Date = input('date in the form DD/MM/YYYY ')
        except ValueError:
            print('ValueError')
            new_data()
        try:
            User_iD = int(input('User ID '))
        except ValueError:
            print('ValueError')
            new_data()
        try:
            cost = float(input('price '))
        except ValueError:
            print('ValueError')
            new_data()
        try:
            Quantity=int(input('Quantity '))
        except ValueError:
            print('ValueError')
            new_data()
        delivered = input('has it been delivered or purchased yes/no')
        delivered = delivered.lower()
        if delivered == 'yes':
            delivered = 'Delivered'
        elif delivered == 'no':
            delivered = 'Total delivered'
        else:
            print('incorrect value')
            system.new_data()
        name_of_item = input('the name of the item')
        Details = input('Extra details')
        new = input('is this a new merchant?(yes or no)')
        new.lower
        with sqlite3.connect('The_database.db') as db2:
            user_find = db2.cursor()
            user_find.execute('select departmentname,Mobilenumber,FirstName,Lastname,Userbuget,Emailaddress from User_database where UseriD=?',(User_iD,))
            user_details = user_find.fetchone()
            find = db2.cursor()
            find.execute('select "CaseNo." from "Totaloverview" ')
            case_number = find.fetchall()
            real_case = len(case_number) + 1
            print(real_case,user_details)
            departmentname = user_details[0]
            Mobilenumber = user_details[1]
            FirstName = user_details[2]
            Lastname = user_details[3]
            Userbuget = user_details[4]
            Emailaddress = user_details[5]
            with sqlite3.connect('The_database.db') as db:
                user_find = db.cursor()
                user_find.execute(
                    'select Departmentbudgetremaining,Dateandtime from "Totaloverview" where departmentID=?',(departmentname,))
                Department_budget_remaining = user_find.fetchall()
                data = []
                for x in range(0, len(Department_budget_remaining)):
                    data.append(list(Department_budget_remaining[x]))
                dates = []
                Department_budget_remaining = []
                for x in range(0, len(data)):
                    count_1 = 1
                    dates.append(data[x][count_1])
                    count_1 = 0
                    Department_budget_remaining.append(data[x][count_1])
                date = [dt.datetime.strptime(x, '%d/%m/%Y').date() for x in dates]
                unixdate = []
                for x in range(0, len(date)):
                    unixdate.append(int(time.mktime(date[x].timetuple())))
                data = list(zip(unixdate, Department_budget_remaining))
                system.sort(data)
                Department_budget_remaining = data[(len(data) - 1)][1]
                Department_budget_remaining = Department_budget_remaining.replace("£", "")
                #print(Department_budget_remaining)
                Department_budget_remaining = int(Department_budget_remaining) - int(cost)
                #print(Department_budget_remaining)
            if Department_budget_remaining <0:
                print('warning the department does not have enough to by this item continue ?')
                option = input('yes/no')
                option = option.lower()
                if option == 'yes':
                    print('understood')
                elif option == 'no':
                    system.main_menu()
                else:
                    print('incorrect value')
                    system.new_data()

        if new == 'yes':
            print('please fill in this data and they will be added to the database')
            try:
                phone = int(input('contact number'))
            except ValueError:
                print('ValueError')
                new_data()
            name = input('Name')
            web = input('web link if any else please enter NA')
            try:
                bank = int(input('Bank details(please do not enter other characters but numbers'))
            except ValueError:
                print('ValueError')
                system.new_data()
            with sqlite3.connect('The_database.db') as db6:
                find2 = db6.cursor()
                find2.execute('select "merchantID" from Merchants')
                merchantID = find2.fetchall()
                real_ID = len(merchantID) + 1
    #view here---->
            mer_add=(real_ID,phone,name,web,bank)
            with sqlite3.connect('The_database.db') as db4:
                cursor = db4.cursor()
                sql = 'insert into "Merchants" (MerchantID,Mobilenumberofmerchant,merchantname,Webaddressifany,Bankdetails) values (?,?,?,?,?)'
                cursor.execute(sql, mer_add)
                db4.commit()
                add = (Date, real_case, User_iD, departmentname, FirstName, Lastname, Userbuget, Mobilenumber, Emailaddress,cost, Quantity, delivered, Department_budget_remaining, name_of_item, Details, real_ID, phone, name, web, bank)
            with sqlite3.connect('The_database.db') as db:
                cursor = db.cursor()
                sql = 'insert into "Totaloverview" (Dateandtime,"CaseNo.",UseriD,departmentID,FirstName,Lastname,Userbuget,Mobilenumber,Emailaddress,costofitem,Quantity,"purchased/deliveredyes/no",Departmentbudgetremaining,nameofitem,"Details",MerchantID,Mobilenumberofmerchant,merchantname,Webaddressifany,Bankdetails) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                cursor.execute(sql, add)
                db.commit()
            add=(Date, real_case, User_iD,cost, Quantity, delivered, Department_budget_remaining, name_of_item, Details, real_ID)
            with sqlite3.connect('The_database.db') as db:
                cursor = db.cursor()
                sql = 'insert into Details (Dateandtime,"CaseNo.",UseriD,costofitem,Quantity,"purchased/deliveredyes/no",Departmentbudgetremaining,nameofitem,"Details",MerchantID) values (?,?,?,?,?,?,?,?,?)'
                cursor.execute(sql, add)
                db.commit()
        if new == 'no':
            ID = int(input('enter their merchant ID'))
            with sqlite3.connect('The_database.db') as db3:
                mer_find = db3.cursor()
                mer_find.execute('select * from Merchants where MerchantID=?',(ID,))
                merde = mer_find.fetchone()
                real_ID=merde[0]
                phone=merde[1]
                name=merde[2]
                web=merde[3]
                bank=merde[4]
            add=(Date,real_case,User_iD,departmentname,FirstName,Lastname,Userbuget,Mobilenumber,Emailaddress,cost,Quantity,delivered,Department_budget_remaining,name_of_item,Details,real_ID,phone,name,web,bank)
            with sqlite3.connect('The_database.db') as db5:
                cursor = db5.cursor()
                sql = 'insert into "Totaloverview" (Dateandtime,"CaseNo.",UseriD,departmentID,FirstName,Lastname,Userbuget,Mobilenumber,Emailaddress,costofitem,Quantity,"purchased/deliveredyes/no",Departmentbudgetremaining,nameofitem,"Details",MerchantID,Mobilenumberofmerchant,merchantname,Webaddressifany,Bankdetails) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                cursor.execute(sql, add)
                db5.commit()
        else:
            print('invalid option')
            system.new_data()
        start_up.main_menu()
    def department():
        ID = input('please enter the department ID ')
        i=0
        with sqlite3.connect('The_database.db') as db2:
            user_find = db2.cursor()
            user_find.execute('select Dateandtime,"CaseNo.",UseriD,costofitem,Quantity from totaloverview where departmentID=?',(ID,))
            data = user_find.fetchall()
            print('Date CaseNo. User ID    cost of item    Quantity')
            while i!=(len(data)):
                print(data[i])
                i+=1
        system.main_menu()
    def user_data():
        print('please choose one of the following options')
        print('To add user to database enter 1')
        print('To find user details enter 2')
        print('To edit a users details enter 3')
        print('to view graph for user expenditure enter 4')
        print('to return to main menu enter 5')
        option = int(input())
        while option > 5 or option == 0:
            print('incorrect value')
            user_details()
            break
        try:
            if option == 1:
                system.add_user()
            elif option == 2:
                system.user_details()
            elif option == 3:
                system.user_details_edit()
            elif option == 4:
                system.expendture()
            elif option == 5:
                system.main_menu()
            else:
                print('invaild option')
                system.main_menu()
        except ValueError:
            print('ValueError')
            system.user_details()

    def add_user():
        department_ID = input('the department')
        First_Name = input('first Name')
        Last_name = input('last Name')
        try:
            User_buget = int(input('what is there buget?'))
        except ValueError:
            print('ValueError')
            add_user()
        try:
            moblie = int(input('phone number?'))
        except ValueError:
            print('ValueError')
        Email_address = input('Email')
        password = input('please enter the users password')
        if password=='' or Email_address=='' or moblie=='' or User_buget=='' or First_Name=='' or Last_name=='' or department_ID=='':
            print('missing data please enter again')
            add_user()
        encoded_passowrd = password.encode('utf-8')
        password = hashlib.md5(encoded_passowrd).hexdigest()
        with open("User_ID_Passwords.csv", "r") as file:
            read = csv.reader(file, delimiter='\t')
            # next(read)
            rowcount = sum(1 for line in read)
        print('There unique user id is', rowcount)
        with open('User_ID_Passwords.csv', 'a', newline='') as csvfie:
            writ = csv.writer(csvfie, delimiter='\t')
            writ.writerow([rowcount, password,First_Name,])
        add = (rowcount, department_ID, First_Name, Last_name, User_buget, moblie, Email_address)
        with sqlite3.connect('The_database.db') as db:
            cursor=db.cursor()
            sql= 'insert into User_database(UseriD,departmentname,Mobilenumber,FirstName,Lastname,Userbuget,Emailaddress) values (?,?,?,?,?,?,?)'
            cursor.execute(sql,add)
            db.commit()
        system.main_menu()
    def user_details():
        User_iD=int(input('please enter thire user ID'))
        with sqlite3.connect('The_database.db') as db2:
            user_find = db2.cursor()
            user_find.execute('select departmentname,Mobilenumber,FirstName,Lastname,Userbuget,Emailaddress from User_database where UseriD=?',(User_iD,))
            user_details = user_find.fetchone()
        print(user_details)
        try:
            home=int(input('enter 1 tor return home'))
        except ValueError:
            print('Value Error')
            user_details()
        system.main_menu()

    def user_details_edit():
        user_details=[]
        print('please enter there new data leave blank to keep the same')
        try:
            User_iD=int(input('please enter there user ID'))
        except ValueError:
            user_details_edit()
        with sqlite3.connect('The_database.db') as db:
            user_find = db.cursor()
            user_find.execute('select departmentname,Mobilenumber,FirstName,Lastname,Userbuget,Emailaddress from User_database where UseriD=?',(User_iD,))
            user_details = user_find.fetchone()
        user_details=list(user_details)
        department_ID = input('the department')
        if department_ID!='':
            user_details[0]=department_ID
        moblie = input('phone number?')
        if moblie != '':
            user_details[1] = moblie
        First_Name = input('first Name')
        if First_Name!='':
            user_details[2]=First_Name
        Last_name = input('last Name')
        if Last_name!='':
            user_details[3]=Last_name
        User_buget =input('what is there budget?')
        if User_buget != '':
            user_details[4] = User_buget
        Email_address = input('Email')
        if Email_address!='':
            user_details[5]=Email_address
        password=input('new password')
        if password!='':
            encoded_password = password.encode('utf-8')
            password = hashlib.md5(encoded_password).hexdigest()
            with open('User_ID_Passwords.csv', 'r') as read:
                reader = csv.reader(read, delimiter='\t')
                with open('User_ID_Passwords_new.csv', 'w', newline='') as edit:
                    writ = csv.writer(edit, delimiter='\t')
                    for row in reader:
                        if row[0] == str(User_iD):
                            row[1] = password
                            writ.writerow(row)

                        else:
                            writ.writerow(row)

            with open('User_ID_Passwords_new.csv', 'r') as read2:
                rea = csv.reader(read2, delimiter='\t')
                with open('User_ID_Passwords.csv', 'w', newline='') as replace:
                    writ = csv.writer(replace, delimiter='\t')
                    for row in rea:
                        writ.writerow(row)
        user_details.append(User_iD)
        print(user_details)
        with sqlite3.connect('The_database.db') as db2:
            user_new = db2.cursor()
            user_update=("update User_database set departmentname=?,Mobilenumber=?,FirstName=?,Lastname=?,Userbuget=?,Emailaddress=? where UseriD=?")
            user_new.execute(user_update,user_details)
            db.commit()

    def expendture():
        ID=input('please enter the user ID ')
        dates_main = []
        cost_main = []
        with sqlite3.connect('The_database.db') as db2:
            find_date = db2.cursor()
            find_date.execute('select Dateandtime from Totaloverview where UseriD=?',(ID,))
            date = find_date.fetchall()
            find_cost = db2.cursor()
            find_cost.execute('select costofitem from Totaloverview where UseriD=?',(ID,))
            cost = find_cost.fetchall()
        with open('graph_one.csv','w+',newline='') as graphing:
            graph = csv.writer(graphing,delimiter=',')
            for x in range(0, len(cost)):
                graph.writerow(date[x])
                graph.writerow(cost[x])
        with open('graph_one.csv', 'r') as csvdata:
            read = csv.reader(csvdata)
            count = 0
            for line in read:
                count += 1
                if count % 2 == 0:
                    cost_main.append(line)
                else:
                    dates_main.append(line)
        a = np.array(dates_main)
        b = a.ravel()
        # print(b)
        c = np.array(cost_main)
        price = c.ravel()
        # print(cost_main)
        date = [dt.datetime.strptime(d, '%d/%m/%Y').date() for d in b]
        price = list(map(int, price))
        check = True
        while check == True:
            check = False
            for j in range(len(date) - 1):
                if date[j] > date[j + 1]:
                    price[j], price[j + 1] = price[j + 1], price[j]
                    date[j], date[j + 1] = date[j + 1], date[j]
                    check = True
        newlist = []
        newlist2 = []
        n = -1
        for i in date:
            n += 1
            #print(n)
            if i not in newlist:
                newlist.append(i)
                newlist2.append(price[date.index(i)])
                #print(newlist2)
                #print(date)
            else:
                index = (len(newlist) - 1)
                #print(price[n])
                #print('newlist', newlist2[index])
                newlist2[index] = newlist2[index] + price[n]
                #print('new vlaue', newlist2[index])
        #print('')
        #print('')
        print(newlist2)
        print(newlist)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.plot(newlist, newlist2)
        plt.gcf().autofmt_xdate()
        plt.show()
        system.main_menu()
    def orders():
        print('please choose one of the following options')
        print('To view pending orders enter 1')
        print('To add order enter 2')
        print('To view all orders 3')
        print('to return to main menu enter 4')
        option = int(input())
        while option > 4 or option == 0:
            print('incorrect value')
            user_details()
            break
        try:
            if option == 1:
                pending()
            elif option == 2:
                new_data()
            elif option == 3:
                orders_view()
            elif option == 4:
                main_menu()
            else:
                print('invaild option')
                main_menu()
        except ValueError:
            print('ValueError')
            orders()

    def orders_view():
        with sqlite3.connect('The_database.db') as db:
            find_date = db.cursor()
            find_date.execute('select * from details')
            data = find_date.fetchall()
            for i in range(0,len(data)-1):
                print(data[i])

    def pending():
        with sqlite3.connect('The_database.db') as db:
            find_date = db.cursor()
            find_date.execute('select * from Details where "purchased/deliveredyes/no"="Not delivered"')
            data = find_date.fetchall()
            for i in range(0,len(data)):
                print(data[i])

    def graphs():
        print('please choose one of the following options')
        print('To view graph for total spending against time enter 1')
        print('To view graph for department spending against time enter 2')
        print('To view graph for a specific months spending against time enter 3 ')
        print('to return to main menu enter 4')
        option = int(input())
        while option > 4 or option == 0:
            print('incorrect value')
            user_details()
            break
        try:
            if option == 1:
                system.graph_total()
            elif option == 2:
                department=input('there department ID')
                system.graph_department(department)
            elif option == 3:
                system.graph_month()
            elif option == 4:
                start_up.main_menu()
            else:
                print('invaild option')
                start_up.main_menu()
        except ValueError:
            print('ValueError')
            system.graphs()
    #http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
    def sort(data):
        if len(data)>1:
            Mid = len(data)//2
            l=data[:Mid]
            r=data[Mid:]
            system.sort(l)
            system.sort(r)
            z=0
            x=0
            c=0
            while z<len(l) and x<len(r):
                if l[z][0]<r[x][0]:
                    data[c]=l[z]
                    z+=1
                else:
                    data[c]=r[x]
                    x+=1
                c+=1
            while z<len(l):
                data[c]=l[z]
                z+=1
                c+=1
            while x<len(r):
                data[c]=r[x]
                x+=1
                c+=1
    def graph_total():
        dates_main = []
        cost_main = []
        with sqlite3.connect('The_database.db') as db2:
            find_date = db2.cursor()
            find_date.execute('select Dateandtime from Totaloverview')
            date = find_date.fetchall()
            find_cost = db2.cursor()
            find_cost.execute('select costofitem from Totaloverview')
            cost = find_cost.fetchall()
        with open('graph_one.csv', 'w+', newline='') as graphing:
            graph = csv.writer(graphing, delimiter=',')
            for x in range(0, len(cost)):
                graph.writerow(date[x])
                graph.writerow(cost[x])
        with open('graph_one.csv', 'r') as csvdata:
            read = csv.reader(csvdata)
            count = 0
            for line in read:
                count += 1
                if count % 2 == 0:
                    cost_main.append(line)
                else:
                    dates_main.append(line)
        a = np.array(dates_main)
        dates = a.ravel()
        # print(b)
        c = np.array(cost_main)
        price = c.ravel()
        # print(cost_main)
        date = [dt.datetime.strptime(x, '%d/%m/%Y').date() for x in dates]
        price = list(map(int, price))
        # check = True
        # while check == True:
        #    check = False
        #    for j in range(len(date) - 1):
        #        if date[j] > date[j + 1]:
        #            price[j], price[j + 1] = price[j + 1], price[j]
        #            date[j], date[j + 1] = date[j + 1], date[j]
        #            check = True
        unixdate = []
        for x in range(0, len(date)):
            unixdate.append(int(time.mktime(date[x].timetuple())))
        #print(unixdate, 'unixdate')
        data = list(zip(unixdate, price))
        system.sort(data)
        #print(data, 'sorted')
        unixdate = []
        price = []
        for x in range(0, len(data)):
            count_1 = 0
            unixdate.append(data[x][count_1])
            count_1 = 1
            price.append(data[x][count_1])

        dates = []
        for x in range(0, len(unixdate)):
            dates.append(dt.datetime.fromtimestamp(int(unixdate[x])).strftime('%d-%m-%Y'))
        #print(dates, 'check')
        date = [dt.datetime.strptime(x, '%d-%m-%Y').date() for x in dates]
        newlist = []
        newlist2 = []
        n = -1
        for i in date:
            n += 1
            # print(n)
            if i not in newlist:
                newlist.append(i)
                newlist2.append(price[date.index(i)])
                # print(newlist2)
                # print(date)
            else:
                index = (len(newlist) - 1)
                # print(price[n])
                # print('newlist', newlist2[index])
                newlist2[index] = newlist2[index] + price[n]
                # print('new vlaue', newlist2[index])
        # print('')
        # print('')
        print(newlist2)
        print(newlist)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
        plt.plot(newlist, newlist2)
        plt.gcf().autofmt_xdate()
        plt.show()
        system.main_menu()

    def graph_department(department):
        ID=department
        dates_main = []
        cost_main = []
        with sqlite3.connect('The_database.db') as db2:
            find_date = db2.cursor()
            find_date.execute('select Dateandtime from Totaloverview where departmentID=?',(ID,))
            date = find_date.fetchall()
            find_cost = db2.cursor()
            find_cost.execute('select costofitem from Totaloverview where departmentID=?',(ID,))
            cost = find_cost.fetchall()
        with open('graph_one.csv', 'w+', newline='') as graphing:
            graph = csv.writer(graphing, delimiter=',')
            for x in range(0, len(cost)):
                graph.writerow(date[x])
                graph.writerow(cost[x])
        with open('graph_one.csv', 'r') as csvdata:
            read = csv.reader(csvdata)
            count = 0
            for line in read:
                count += 1
                if count % 2 == 0:
                    cost_main.append(line)
                else:
                    dates_main.append(line)
        a = np.array(dates_main)
        b = a.ravel()
        # print(b)
        c = np.array(cost_main)
        price = c.ravel()
        # print(cost_main)
        date = [dt.datetime.strptime(d, '%d/%m/%Y').date() for d in b]
        price = list(map(int, price))
        unixdate = []
        for x in range(0, len(date)):
            unixdate.append(int(time.mktime(date[x].timetuple())))
        print(unixdate, 'unixdate')
        data = list(zip(unixdate, price))
        system.sort(data)
        print(data, 'sorted')
        unixdate = []
        price = []
        for x in range(0, len(data)):
            count_1 = 0
            unixdate.append(data[x][count_1])
            count_1 = 1
            price.append(data[x][count_1])
        dates = []
        for x in range(0, len(unixdate)):
            dates.append(dt.datetime.fromtimestamp(int(unixdate[x])).strftime('%d-%m-%Y'))
        print(dates, 'check')
        date = [dt.datetime.strptime(x, '%d-%m-%Y').date() for x in dates]
        newlist = []
        newlist2 = []
        n = -1
        for i in date:
            n += 1
            #print(n)
            if i not in newlist:
                newlist.append(i)
                newlist2.append(price[date.index(i)])
                # print(newlist2)
                # print(date)
            else:
                index = (len(newlist) - 1)
                # print(price[n])
                # print('newlist', newlist2[index])
                newlist2[index] = newlist2[index] + price[n]
                # print('new vlaue', newlist2[index])
        print(newlist2)
        print(newlist)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.plot(newlist, newlist2)
        plt.gcf().autofmt_xdate()
        plt.show()
        system.main_menu()
    def graph_month():
        dates_main=[]
        cost_main=[]
        month1='%'+input('please enter the month you with to look at in the form MM/YYYY')
        print(month1)
        with sqlite3.connect('The_database.db') as db2:
            find_date = db2.cursor()
            find_date.execute('select Dateandtime from Totaloverview where Dateandtime LIKE ?', (month1,))
            date = find_date.fetchall()
            find_cost = db2.cursor()
            find_cost.execute('select costofitem from Totaloverview where Dateandtime LIKE ?', (month1,))
            cost = find_cost.fetchall()
            print(date)
            print(cost)
        with open('graph_one.csv', 'w+', newline='') as graphing:
            graph = csv.writer(graphing, delimiter=',')
            for x in range(0, len(cost)):
                graph.writerow(date[x])
                graph.writerow(cost[x])
        with open('graph_one.csv', 'r') as csvdata:
            read = csv.reader(csvdata)
            count = 0
            for line in read:
                count += 1
                if count % 2 == 0:
                    cost_main.append(line)
                else:
                    dates_main.append(line)
        a = np.array(dates_main)
        b = a.ravel()
        # print(b)
        c = np.array(cost_main)
        price = c.ravel()
        # print(cost_main)
        date = [dt.datetime.strptime(d, '%d/%m/%Y').date() for d in b]
        price = list(map(int, price))
        unixdate = []
        for x in range(0, len(date)):
            unixdate.append(int(time.mktime(date[x].timetuple())))
        print(unixdate, 'unixdate')
        data = list(zip(unixdate, price))
        system.sort(data)
        print(data, 'sorted')
        unixdate = []
        price = []
        for x in range(0, len(data)):
            count_1 = 0
            unixdate.append(data[x][count_1])
            count_1 = 1
            price.append(data[x][count_1])

        dates = []
        for x in range(0, len(unixdate)):
            dates.append(dt.datetime.fromtimestamp(int(unixdate[x])).strftime('%d-%m-%Y'))
        print(dates, 'check')
        date = [dt.datetime.strptime(x, '%d-%m-%Y').date() for x in dates]
        newlist = []
        newlist2 = []
        n = -1
        for i in date:
            n += 1
            # print(n)
            if i not in newlist:
                newlist.append(i)
                newlist2.append(price[date.index(i)])
                # print(newlist2)
                # print(date)
            else:
                index = (len(newlist) - 1)
                # print(price[n])
                # print('newlist', newlist2[index])
                newlist2[index] = newlist2[index] + price[n]
                # print('new vlaue', newlist2[index])
        print(newlist2)
        print(newlist)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.plot(newlist, newlist2)
        plt.gcf().autofmt_xdate()
        plt.show()
        start_up.main_menu()
#passowrd()
#start_up.main_menu()
start_up.login()
#add_user()
#system.new_data()
#main_menu()
#user_details()
#search()
#system.user_details_edit()
#graphs()
#orders()
#system.graph_total()
#graph_department()
#pending()
#expendture()
#system.graph_month()
#system.today_overview()
#system.total_overview()
#TO DO
#take away user and department beget for each perches
#add into basic
#add pending data from new data
# in search have an output with all variables considered
#chage int to float where needed
#look at edit user data
