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
    sql3 = """INSERT INTO SUSPECTS(USER_ID,LOCATION) VALUES (\'%d\',\'%s\')""" \
           % (u, lo)
    sql4 = """INSERT INTO ZONE_SELECT(USER_ID,LOCATION) VALUES (\'%d\',\'%s\')""" \
           % (u, lo)
    try:
        cursor.execute(sql1)
        connection.commit()
        cursor.execute(sql2)
        connection.commit()
        cursor.execute(sql3)
        connection.commit()
        cursor.execute(sql4)
        connection.commit()
        print("Your Data is Inserted Into Database ! \nThank You For Using Covid-19 Detection System.")
    except Exception as E:
        print(" ! ")


def View():
    passwd = "STANSFORLIFE"
    ch = input("""
    
                    Hello User,
            Please Enter Admin For Observing Data As Admin(Password Required).
            Please Enter Organ For Observing Data As Organisation(Name Required).
            Please Enter Client For Observing Data As Client(UserID Required).
            
            >""")
    if ch.title() == 'Admin':
        p = input("Enter Admin Password :")
        if p == "STANSFORLIFE":
            sql = "SELECT * FROM ADMIN ;"
            try:
                cursor.execute(sql)
                res = cursor.fetchall()
                for record in res:
                    SR = record[0]
                    UD = record[1]
                    FN = record[2]
                    LN = record[3]
                    GD = record[4]
                    TP = record[5]
                    CC = record[6]
                    RN = record[7]
                    SB = record[8]
                    PP = record[9]
                    FT = record[10]
                    ZZ = record[11]
                    LL = record[12]
                    SS = record[13]
                    print("""
                    BASIC INFORMATION -
                        * SERIAL NUMBER : {0}
                        * USER ID : {1}
                        * NAME : {2} {3}
                        * GENDER : {4}
                        * LOCATION : {11}
                    THE SYMPTOMS -
                        * LAST RECORDED TEMPERATURE : {5}
                        * COUGH : {6}
                        * RUNNING NOSE : {7}
                        * SHORT OF BREATH : {8}
                    OTHER AFFECTING FACTORS :
                        * PREGNANCY STATUS : {9}
                        * FOREIGN TRAVEL HISTORY : {10}
                    ABOUT ZONE AND SUSPECTING :
                        * ZONE : {12}
                        * SUSPECT : {13} 
                    """.format(SR, UD, FN, LN, GD, TP, CC, RN, SB, PP, FT, LL, ZZ, SS))
            except Exception as E:
                print("Exception : %s" % E)


Insert_info()
View()
