from flask import Flask, render_template,request
import mysql.connector  # Import MySql Connector
from datetime import datetime

app = Flask(__name__)

# assigning data for the SQL connector
url = "mytestdatabase.cme7o154w5f8.ap-south-1.rds.amazonaws.com"
username = "admin"  # input("Enter User name ")
password = "passw0rd"  # input("Inser your password ")
db = "MyTicketDB"
mydb = mysql.connector.connect(
    host=url, user=username, passwd=password, database=db)


# Create connection with database
def DBConnection():
    try:
        if (mydb.is_connected() == True):
            print("DB connection Sucessful !!!")
            return True

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


@app.route("/")  # Index page
def Dashboard():
    # Load the data to table

    try:
        if(DBConnection() == True):
            mycursor = mydb.cursor()
            mycursor.execute("Select * from TicketTable")
            if True:
                userdata=mycursor.fetchall()
                return render_template('index.html',userdata=userdata)
    except mysql.connector.Error as err:
             print("Something went wrong: {}".format(err))
             return render_template('index.html')




@app.route('/add', methods= ['GET','POST'])
def addData():
    print("Test Pass")
    if (request.method == 'POST'):
        name= request.form['agentName']
        issue= request.form['issue']
        priority= request.form['radio1']
        status=request.form['Status Type']

        print(name,issue,priority,status)
        print("begin to execute and inside if")

       
        try:

          if(DBConnection() == True):
                mycursor = mydb.cursor()
                print("begin to execute")
                mycursor.execute(f"INSERT INTO TicketTable (TicketNo, priority, Status, AgentID, Issue, createdate) VALUES ('{2}','{priority}','{status}','{name}','{issue},'{datetime}')")
                # INSERT INTO TicketTable (TicketNo, priority, Status, AgentID, Issue, createdate) VALUES ('1','High','Resolve','20123459','Not power on','2021/05/07')
                mydb.commit()
                print("begin to execute")
                return "Sucess"
        except mysql.connector.Error as err:
             print("Something went wrong: {}".format(err))

    else:
        print("not added")




if __name__ == "__main__":
    app.run(debug=True)
