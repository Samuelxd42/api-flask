from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, ListHabilidades


app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {
        'id': 0,
        'nome':'Samuel',
        'hablidades':['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Fernandes',
        'habilidades': ['Pythin', 'Django']
    }
]


class Devenvolvedor(Resource):
    def get(self, id):

        try:
            response = desenvolvedores[id]

        except IndexError:
            mensagem = 'Desendor de ID {} não exite'.format(id)
            response = {'status': 'erro', 'messagem': mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'messagem': mensagem}
        
        return response


    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados


    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'messagem': 'registro excluido'}
        

class ListDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])



api.add_resource(Devenvolvedor, '/dev/<int:id>/')
api.add_resource(ListDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')
api.add_resource(ListHabilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)

