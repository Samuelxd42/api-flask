from flask import Flask, request
from flask.json import jsonify
import json


app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome':'Samuel',
        'hablidades':['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Fernandes',
        'habilidades': ['Pythin', 'Django']
    }
]

@app.route('/dev/<int:id>',  methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:

            response = desenvolvedores[id]
            return jsonify(response)

        except IndexError:
            mensagem = 'Desendor de ID {} não exite'.format(id)
            response = {'status': 'erro', 'messagem': mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'messagem': mensagem}

        return jsonify(response)

    elif request.method == 'PUT':

        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method =='DELETE':

        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'messagem': 'registro excluido'})


@app.route('/dev/', methods=['POST', 'GET'])
def list_desenvolvedore():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__=='__main__':
    app.run(debug=True)

