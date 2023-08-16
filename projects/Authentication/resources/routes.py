from resources.resources import UserApi,LoginApi

def initialize_routes(api):
    api.add_resource(UserApi,"/api/User")
    api.add_resource(LoginApi, '/api/Login')