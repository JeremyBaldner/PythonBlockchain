from flask import Flask, jsonify, request
from uuid import uuid4
from blockchain import Blockchain

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    # run the PoW algo
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # get reward for solving a block
    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)

    # add a new block to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    # create response
    response = {
        'message': "New block forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    # return response
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    # get values from request
    values = request.get_json()

    # verify all values are present
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Missing values", 400

    # create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    # create and return response
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 200


# return the full chain
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


# create a new node
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


# consensus algo
@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
