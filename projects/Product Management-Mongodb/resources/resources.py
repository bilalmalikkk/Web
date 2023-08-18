from flask import request,Response, jsonify
from flask_restful import Resource
from database.models import productPractise

class productpracticeApi(Resource):
    def get(self):
        prod = productPractise.objects().to_json()
        return Response(prod, mimetype="application/json", status=200)
    def post(self):
        data=request.get_json()
        pro =productPractise(**data)
        pro.save()

class productpracticeApiwithparam(Resource):
    def get(self, id):
        pro = productPractise.objects.get(id=id).to_json()
        return Response(pro, mimetype="application/json", status=200)

    def put(self, id):
        data = request.get_json()
        print(data)
        print(id)
        print(productPractise.objects.get(name=id))
        productPractise.objects.get(name=id).update(**data)

    def delete(self, id):
        productPractise.objects.get(name=id).delete()
