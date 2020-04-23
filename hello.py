from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit', methods = ['POST','GET'])
def login(): 
    if request.method  == "POST":
        data = request.form.to_dict()
        filetocsv(data)
        return redirect("./thankyou.html")
    else:
        return "some thing went wrong"

def filetodatabase(data):
    with open("database.txt",mode = "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data ["message"]
        file=database.write(f"\nEMAIL-{email},SUBJECT-{subject},MESSAGE-{message}")
        
def filetocsv(data):
    with open("datbase.csv",mode = "a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data ["message"]
        csv_writer=csv.writer(database2,delimiter="," ,quotechar = '"' ,quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])