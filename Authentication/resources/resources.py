from flask import Response, jsonify, request
from flask_restful import Resource
from database.models import User


class UserApi(Resource):
    def post(self):
        body=request.get_json()
        try: 
            res = User.objects.get(email=body["email"]).to_json()
            if res:
                return {"error":"User already exists"},404
        except User.DoesNotExist: 
                user1 = User(fullName=body["fullName"],email=body["email"],password=body["password"],phone=body["phone"],cnic=body["cnic"]).save()
                id=user1.id
                return {'id':str(id)},200
    def get(self):
        usr=User.objects().to_json()
        return Response(usr, mimetype="application/json", status=200)

class LoginApi(Resource):
    def post(self):
        try:
            body=request.get_json()
            usr=User.objects.get(email=body.get('email') , password=body.get('password')).to_json()
            return Response(usr, mimetype="application/json", status=200)
        except User.DoesNotExist:
             return {"error":"User dont exists"},400