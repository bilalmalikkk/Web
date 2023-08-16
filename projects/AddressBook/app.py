from flask import Flask, render_template, request, make_response
from contact import Contact
from controller import add_Contact, isValidate, show_contacts, show_contact_name

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=["GET", "POST"])
def contacts():
    return render_template("contact.html")

@app.route('/searchContact', methods=["GET", "POST"])
def searchContact():
    return render_template("searchContact.html")

@app.route('/addContact', methods=["POST"])
def addContact():
    name = request.form["name"]
    mobileNo = request.form["MobileNo"]
    cit = request.form["city"]
    profes = request.form["profession"]
    Con = Contact(name, mobileNo, cit, profes)
    add_Contact(Con)
    response = make_response(render_template("addContact.html"))
    response.set_cookie("uname", name)
    response.set_cookie("ucity", cit)
    return response

@app.route('/showContact', methods=["GET", "POST"])
def showContact():
    name = request.cookies.get("uname")
    cit = request.cookies.get("ucity")
    data = show_contacts()
    result = []
    for item in data:
        dic = {
            "name": item[1],
            "MobileNo": item[2],
            "city": item[3],
            "profession": item[4]
        }
        result.append(dic)
    return render_template("showContact.html", context=result, name=name, city=cit)

@app.route('/searchComp', methods=["POST"])
def searchComp():
    name = request.form["name"]
    data = show_contact_name(name)
    result = [{
        "name": data[1],
        "MobileNo": data[2],
        "city": data[3],
        "profession": data[4]
    }]
    return render_template("searchComp.html", context=result)

def cleverFunction():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
