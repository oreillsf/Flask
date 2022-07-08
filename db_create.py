import pymysql

conn = pymysql.connect(
        host= 'database2.xxxxxx.eu-west-1.rds.amazonaws.com', 
        port = 3306,
        user = 'xxxxx', 
        password = 'xxxxxxx',
        db = 'practicum',
        
        )

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Consent (choice1 varchar(10),choice2 varchar(10),choice3 varchar(10),choice4 varchar(10),choice5 varchar(10),choice6 varchar(10) )

# """
# cursor.execute(create_table)

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Questionnaire (q1 varchar(10),q2 varchar(10),q3 varchar(10),q4 varchar(10),q5a varchar(10),q5b varchar(10),q5c varchar(10),q5d varchar(10),pinComment5a varchar(300),pinComment5b varchar(300),pinComment5c varchar(300),pinComment5d varchar(300),q6 varchar(10),q7 varchar(10),pinComment6 varchar(300),pinComment7 varchar(300) )

# """
# cursor.execute(create_table)

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Password (username varchar(20),password varchar(8) )

# """
# cursor.execute(create_table)

# Table Creation
# cursor=conn.cursor()
# create_table="""
# create table PasswordSuccess (firstattempt varchar(5),secondattempt varchar(5),thirdattempt varchar(5) )

# """
# cursor.execute(create_table)

# Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Pin (username varchar(20),pin varchar(4) )

# """
# cursor.execute(create_table)

# # Table Creation
# cursor=conn.cursor()
# create_table="""
# create table PinSuccess (firstattempt varchar(5),secondattempt varchar(5),thirdattempt varchar(5) )

# """
# cursor.execute(create_table)

# Table Creation
# cursor=conn.cursor()
# create_table="""
# create table MusicalSuccess (firstattempt varchar(5),secondattempt varchar(5),thirdattempt varchar(5) )

# """
# cursor.execute(create_table)

# #Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Musical (username varchar(20),music varchar(8) )

# """
# cursor.execute(create_table)

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Survey (q1 varchar(10),q2 varchar(10),q3 varchar(10),q4 varchar(10), pinComment1 varchar(300),pinComment2 varchar(300),pinComment3 varchar(300),pinComment4 varchar(300),pinComment5 varchar(500) )

# """
# cursor.execute(create_table)

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Graphical (username varchar(20), imgs varchar(50) )

# """
# cursor.execute(create_table)

# Table Creation
# cursor=conn.cursor()
# create_table="""
# create table GraphicalSuccess (firstattempt varchar(5),secondattempt varchar(5),thirdattempt varchar(5) )
# """
# cursor.execute(create_table)


#insert query
def insert_details(choice1,choice2,choice3,choice4,choice5,choice6):
    cur=conn.cursor()
    cur.execute("INSERT INTO Consent (choice1,choice2,choice3,choice4,choice5,choice6) VALUES (%s,%s,%s,%s,%s,%s)", (choice1,choice2,choice3,choice4,choice5,choice6))
    conn.commit()

#read the data
def get_passdetails(username,password):
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Password WHERE username = %s AND password = %s", (username, password))
    details = cur.fetchone()
    if details:
    	return 'true'
    else: 	
    	return 'false'


#insert query
def insert_questdetails(ansQ1,ansQ2,ansQ3,ansQ4,ansQ5a,ansQ5b,ansQ5c,ansQ5d,ansQComm5a,ansQComm5b,ansQComm5c,ansQComm5d,ansQ6,ansQ7,ansQ6Comm,ansQ7Comm):
    cur=conn.cursor()
    cur.execute("INSERT INTO Questionnaire (q1,q2,q3,q4,q5a,q5b,q5c,q5d,pinComment5a,pinComment5b,pinComment5c,pinComment5d,q6,q7,pinComment6,pinComment7) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ansQ1,ansQ2,ansQ3,ansQ4,ansQ5a,ansQ5b,ansQ5c,ansQ5d,ansQComm5a,ansQComm5b,ansQComm5c,ansQComm5d,ansQ6,ansQ7,ansQ6Comm,ansQ7Comm))
    conn.commit()

#insert query
def insert_passdetails(username,password):
    cur=conn.cursor()
    cur.execute("INSERT INTO Password (username,password) VALUES (%s,%s)", (username,password))
    conn.commit()

def insert_passsuccess(firstattempt,secondattempt,thirdattempt):
    cur=conn.cursor()
    cur.execute("INSERT INTO PasswordSuccess (firstattempt,secondattempt,thirdattempt) VALUES (%s,%s,%s)", (firstattempt,secondattempt,thirdattempt))
    conn.commit()


#insert query
def insert_pindetails(username,pin):
    cur=conn.cursor()
    cur.execute("INSERT INTO Pin (username,pin) VALUES (%s,%s)", (username,pin))
    conn.commit()

#read the data
def get_pindetails(username,pin):
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Pin WHERE username = %s AND pin = %s", (username, pin))
    details = cur.fetchone()
    if details:
    	return 'true'
    else: 	
    	return 'false'


def insert_pinsuccess(firstattempt,secondattempt,thirdattempt):
    cur=conn.cursor()
    cur.execute("INSERT INTO PinSuccess (firstattempt,secondattempt,thirdattempt) VALUES (%s,%s,%s)", (firstattempt,secondattempt,thirdattempt))
    conn.commit()


def insert_musicaldetails(username,musicName):
    cur=conn.cursor()
    cur.execute("INSERT INTO Musical (username,music) VALUES (%s,%s)", (username,musicName))
    conn.commit()

#read the data
def get_musicaldetails(username,musicName):
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Musical WHERE username = %s AND music = %s", (username, musicName))
    details = cur.fetchone()
    if details:
        return 'true'
    else:   
        return 'false'


def insert_musicalsuccess(firstattempt,secondattempt,thirdattempt):
    cur=conn.cursor()
    cur.execute("INSERT INTO MusicalSuccess (firstattempt,secondattempt,thirdattempt) VALUES (%s,%s,%s)", (firstattempt,secondattempt,thirdattempt))
    conn.commit()

#insert query
def insert_surdetails(ansQ1,ansQ2,ansQ3,ansQ4,ansQ1Comm,ansQ2Comm,ansQ3Comm,ansQ4Comm,ansQ5Comm):
    cur=conn.cursor()
    cur.execute("INSERT INTO Survey (q1,q2,q3,q4,pinComment1,pinComment2,pinComment3,pinComment4,pinComment5) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ansQ1,ansQ2,ansQ3,ansQ4,ansQ1Comm,ansQ2Comm,ansQ3Comm,ansQ4Comm,ansQ5Comm))
    conn.commit()

def insert_graphicaldetails(username,listOfImg):
    cur=conn.cursor()
    cur.execute("INSERT INTO Graphical (username,imgs) VALUES (%s,%s)", (username,listOfImg))
    conn.commit()

def get_graphicaldetails(username,listOfImg):
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Graphical WHERE username = %s AND imgs = %s", (username, listOfImg))
    details = cur.fetchone()
    if details:
        return 'true'
    else:   
        return 'false'

def insert_graphicalsuccess(firstattempt,secondattempt,thirdattempt):
    cur=conn.cursor()
    cur.execute("INSERT INTO GraphicalSuccess (firstattempt,secondattempt,thirdattempt) VALUES (%s,%s,%s)", (firstattempt,secondattempt,thirdattempt))
    conn.commit()







