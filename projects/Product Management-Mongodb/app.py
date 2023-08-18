from flask import Flask, jsonify,request, render_template
from flask_restful import Api,Resource
from database import db
from resources import routes
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/product'
}
api = Api(app)
db.initialize_db(app)
routes.initialize_route(api)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/showProducts')
def showproducts():
    return render_template("showProducts.html")


@app.route('/addProducts')
def addproduct():
    return render_template("addProducts.html")


@app.route('/updateProducts')
def updateproduct():
    return render_template("updateProducts.html")


@app.route('/deleteProducts')
def deleteproduct():
    return render_template("deleteProduct.html")


if __name__ == '__main__':
    app.run()
