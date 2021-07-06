from flask_restful import Resource, request
import json

from werkzeug.wrappers import response


lista_habilidades = [
     {
        'id': 0,
        'hablidades':[
            'Python', 
            'Flask'
        ]
    },
]

class Habilidades(Resource):
    def get(self, id):
        response = lista_habilidades[id]
        return response


    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados


    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'messagem': 'registro excluido'}


class ListHabilidades(Resource):
    def get(self):
        return lista_habilidades

    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return (lista_habilidades[posicao])

