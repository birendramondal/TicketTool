import random
from flask import Flask, render_template, request
import mysql.connector  # Import MySql Connector
from datetime import date, datetime

from werkzeug.utils import redirect

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
                userdata = mycursor.fetchall()
                return render_template('index.html', userdata=userdata)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return render_template('index.html')


# Load the weekly graph

@app.route("/weekdata", methods=["GET", "POST"])
def weekdata():
    weekdata = []
    for i in range(1, 8):
        weekdata.append(random.randint(7, 80))
        data = {
            "weekdata": weekdata
        }
    return data


@app.route('/add', methods=['GET', 'POST'])
def addData():
    print("Test Pass")
    if (request.method == 'POST'):
        name = request.form['agentName']
        issue = request.form['issue']
        priority = request.form['radio1']
        status = request.form['Status Type']
        bddate = datetime.today().strftime('%Y-%m-%d')

        print(name, issue, priority, status, bddate)
        print("begin to execute and inside if")

        try:

            if(DBConnection() == True):
                mycursor = mydb.cursor()
                print("begin to execute")
                # mycursor.execute(f"INSERT INTO TicketTable (TicketNo, priority, Status, AgentID, Issue, createdate) VALUES ('{3}','{priority}','{status}','{name}','{issue}','2021/05/07')")
                mycursor.execute(
                    f"INSERT INTO TicketTable (priority, Status, AgentID, Issue, createdate) VALUES ('{priority}','{status}','{name}','{issue}','{bddate}')")
                # ALTER TABLE TicketTable CHANGE TicketNo TicketNo INT(50)AUTO_INCREMENT -----> Enable Auto increment in RDS
                # mycursor.execute(f"INSERT INTO TicketTable (TicketNo, priority, Status, AgentID, Issue, createdate) VALUES ('5','{priority}','{status}','{name}','{issue}','{bddate}')")
                mydb.commit()
                print("Data comitted to DB")
                return redirect("/")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    else:
        print("not added")


if __name__ == "__main__":
    app.run(debug=True)
