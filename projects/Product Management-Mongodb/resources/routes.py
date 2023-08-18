from .resources import productpracticeApi, productpracticeApiwithparam

def initialize_route(api):
    api.add_resource(productpracticeApi, '/api/pro')
    api.add_resource(productpracticeApiwithparam, '/practice/pro/<id>')