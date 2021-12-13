from flask import Flask,render_template,request
import mysql.connector
test = Flask(__name__)


url = "mytestdatabase.cme7o154w5f8.ap-south-1.rds.amazonaws.com"
username = "admin"#input("Enter User name ")
password = "passw0rd"#input("Inser your password ")
db = "MyTicketDB"
# print("Okay")

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

#Inser The data
@test.route("/", methods= ['GET','POST'])  
def hello_world():
    if request.method == 'POST':
        name= request.form['username']
        email= request.form['email']
        print(name,email)
        if(DBConnection() == True):
            mycursor = mydb.cursor()
            print("begin to execute")
            mycursor.execute(f"INSERT INTO TestTable (name, email) VALUES ('{name}','{email}')")
            mydb.commit()
            return "sucess"

    return render_template("testlogin.html")




#load the data
@test.route("/show", methods=['GET','POST'])
def showTable():
    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute("Select * from TestTable")
        if True:
            userdata=mycursor.fetchall()
            return render_template('showtestdata.html',userdata=userdata)





if __name__ == "__main__":
    test.run(debug=True)