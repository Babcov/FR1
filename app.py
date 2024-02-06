from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

clients = []

@app.route('/')
def index():
    return 'Управление рассылками'

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    client = {
        'id': len(clients) + 1,
        'name': data['name'],
        'email': data['email']
    }
    clients.append(client)
    return jsonify(client), 201

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    client = next((c for c in clients if c['id'] == client_id), None)
    if client:
        client['name'] = data.get('name', client['name'])
        client['email'] = data.get('email', client['email'])
        return jsonify(client), 200
    return jsonify({'message': 'Client not found'}), 404

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = next((c for c in clients if c['id'] == client_id), None)
    if client:
        clients.remove(client)
        return jsonify({'message': 'Client has been deleted'}), 200
    return jsonify({'message': 'Client not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)

