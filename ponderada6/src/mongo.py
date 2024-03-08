from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco']

# Inserção de documentos
colecao = db['minha_colecao']
colecao.insert_one({'nome': 'João', 'idade': 30})
colecao.insert_many([{'nome': 'Maria', 'idade': 25}, {'nome': 'Pedro', 'idade': 35}])

# Busca de documentos
for doc in colecao.find({'idade': {'$gt': 30}}):
    print(doc)

# Atualização de documentos
colecao.update_one({'nome': 'João'}, {'$set': {'idade': 31}})

# Exclusão de documentos
colecao.delete_one({'nome': 'Pedro'})

# Criação de um índice TTL
colecao.create_index([('data_criacao', 1)], expireAfterSeconds=3600)