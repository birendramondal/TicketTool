import mysql.connector #Import MySql Connector

# assigning data for the SQL connector 
url = "mytestdatabase.cme7o154w5f8.ap-south-1.rds.amazonaws.com"
username = "admin"#input("Enter User name ")
password = "passw0rd"#input("Inser your password ")
db = "MyTicketDB"

mydb = mysql.connector.connect(
    host=url, user=username, passwd=password, database=db)

def DBConnection():
    try:
        if (mydb.is_connected() == True):
            # print("DB connection Sucessful !!!")
            return True


    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

def DropTable():
    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * TicketTable")
        # mycursor.execute("CREATE TABLE TicketTable (TicketNo varchar(20) NOT NULL, priority varchar(20), Status varchar(20), AgentID varchar(20), Issue varchar(255), createdate date,PRIMARY KEY(TicketNo));")

        # print("Table deleted Sucessfully !!")
        for i in mycursor:
            print(i)  