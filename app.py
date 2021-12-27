import random
import time
from flask import Flask, render_template, request
import mysql.connector  # Import MySql Connector
from datetime import date, datetime, timedelta

from werkzeug.utils import redirect

app = Flask(__name__)

# assigning data for the SQL connector
url = "mytestdatabase.cme7o154w5f8.ap-south-1.rds.amazonaws.com"
username = "admin"  # input("Enter User name ")
password = "passw0rd"  # input("Inser your password ")
db = "MyTicketDB"
mydb = mysql.connector.connect(
    host=url, user=username, passwd=password, database=db)


def DBConnection():  # *****************Create connection with database*****************
    try:
        if (mydb.is_connected() == True):
            print("DB connection Sucessful !!!")
            return True

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def counter(inputdate):  # *****************Count date column for load the 7 Days Data *****************
    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute(
            f'SELECT COUNT(TicketNo) FROM TicketTable WHERE createdate="{inputdate}"')
       
        if True:
            countdata = mycursor.fetchall()

        res = [lis[0] for lis in countdata]
        time.sleep(0.1)      #****************Add time to load in to the Buffer****************
        return res[0]


@app.route("/")  # Index page
def Dashboard():   # *****************Load the data to table*****************

    try:
        if(DBConnection() == True):
            mycursor = mydb.cursor()
            mycursor.execute("Select * from TicketTable")
            if True:
                userdata = mycursor.fetchall()
                return render_template('index.html', userdata=userdata)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return render_template('index.html')


@app.route("/weekdata", methods=["GET", "POST"])
def weekdata():                         # *****************Load the weekly graph*****************
    weekdata = []
    todaysdate = date.today()
    for i in range(1, 8):
        # weekdata.append(random.randint(7, 80))    ****************Generate Random Graph****************
        weekdata.append(counter(todaysdate))  #****************Call the Counter Function ****************
        todaysdate = todaysdate-timedelta(1)  
        data = {
            "weekdata": weekdata
        }
    return data


@app.route('/add', methods=['GET', 'POST'])   #****************Add Value to the DB****************
def addData():
    if (request.method == 'POST'):
        name = request.form['agentName']
        issue = request.form['issue']
        priority = request.form['radio1']
        status = request.form['Status Type']
        bddate = datetime.today().strftime('%Y-%m-%d')

        try:
            if(DBConnection() == True):
                mycursor = mydb.cursor()
                mycursor.execute(f"INSERT INTO TicketTable (priority, Status, AgentID, Issue, createdate) VALUES ('{priority}','{status}','{name}','{issue}','{bddate}')")
                # ALTER TABLE TicketTable CHANGE TicketNo TicketNo INT(50)AUTO_INCREMENT -----> Enable Auto increment in RDS
                # mycursor.execute(f"INSERT INTO TicketTable (TicketNo, priority, Status, AgentID, Issue, createdate) VALUES ('5','{priority}','{status}','{name}','{issue}','{bddate}')") -----> With Customize Ticket Number 
                mydb.commit()
                return redirect("/")

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    else:
        print("not added")


@app.route('/delete/<int:sno>', methods=['GET', 'POST'])
def updateDB(sno):
    if (request.method == 'POST'):
        TicketNumber = request.form[sno]
        print(TicketNumber)



if __name__ == "__main__":
    app.run(debug=True)