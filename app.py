from flask import Flask, render_template, g
import mysql.connector  # Import MySql Connector

app = Flask(__name__)

# assigning data for the SQL connector
url = "mytestdatabase.cme7o154w5f8.ap-south-1.rds.amazonaws.com"
username = "admin"  # input("Enter User name ")
password = "passw0rd"  # input("Inser your password ")
db = "MyTicketDB"
mydb = mysql.connector.connect(
    host=url, user=username, passwd=password, database=db)


# Create connection
def DBConnection():
    try:
        if (mydb.is_connected() == True):
            print("DB connection Sucessful !!!")
            return True

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


@app.route("/")  # Index page
def Dashboard():
    return render_template('index.html')


# load the data
if __name__ == "__main__":
    app.run(debug=True)
