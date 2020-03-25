import pymysql.cursors

connection = pymysql.connect("localhost", "root", "sarveshsj25", "NEW_COVID")
cursor = connection.cursor()
print(""" *** WELCOME TO USER INTERFACE FOR *** 

              ***  COVID-19 DETECTION SYSTEM    ***  


              """)


def Insert_info():
    u = int(input("Please Enter Your Desired User-ID \n >"))
    f = input("Please Enter Your First Name \n >")
    l = input("Please Enter Your Last Name \n >")
    g = input("Please Enter Your Gender(M/F) \n >")
    t = float(input("Please Enter Your Recorded Body Temperature \n >"))
    c = input("Are You Suffering From Cough ? (Y/n) \n >")
    s = input("Are You Suffering From Short of Breath ? (Y/n) \n >")
    r = input("Are You Suffering From Running Nose ? (Y/n) \n >")
    if g == 'F' or g == 'f':
        p = input("Are You Pregnant ? (Y/n) \n >")
    else:
        p = 'N'
    tr = input("Have You Visited Any Corona Virus (Covid 19 Disease) Affected Country in Past 3 Months ? (Y/n)\n >")
    lo = input("Please Enter Your Locality (Enter Name of Big Locality Like Shivajinagar,Kothrud,etc.) \n > ")
    print("Thanks ! \nYour Whole Information is Gathered.")
    sql1 = """INSERT INTO BASIC_INFO(USER_ID,FIRST_NAME,LAST_NAME,GENDER) VALUES (\'%d\',\'%s\',\'%s\',\'%s\')""" \
           % (u, f, l, g)
    sql2 = """INSERT INTO SYMPTOMS(USER_ID,TEMP,COUGH,RUNNING_NOSE,SHORT_BREATH,PREG,FOREIGN_TRP) VALUES(\'%d\',\'%f\',
            \'%s\',\'%s\',\'%s\',\'%s\',\'%s\')""" \
           % (u, t, c, r, s, p, tr)
    sql3 = """INSERT INTO SUSPECTS(LOCATION) VALUES (\'%s\')""" \
           % lo
    try:
        cursor.execute(sql1)
        connection.commit()
        cursor.execute(sql2)
        connection.commit()
        cursor.execute(sql3)
        connection.commit()
        print("Your Data is Inserted Into Database ! \nThank You For Using Covid-19 Detection System.")
    except Exception as E:
        print(" ! ")


Insert_info()
