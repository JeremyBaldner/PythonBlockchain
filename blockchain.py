import hashlib
import requests
import json
from hashlib import sha256
from time import time
from urllib.parse import urlparse


class Blockchain(object):
    def __init__(self):
        self.chain = [{'index': 0,
                       'timestamp': time(),
                       'transactions': 0,
                       'proof': 0,
                       'previous_hash': 0}]
        self.current_transactions = []
        self.nodes = set()

    # create a new node based on url
    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    # create a new block and add it to the chain.
    def new_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []

        self.chain.append(block)
        return block

    # add a new transaction to the list of transactions.
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    # PoW algo that increments proof value until valid_proof returns true.
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    # verify the current chain has not already been solved
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False

            # verify values in the chain are correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1
        return True

    # consensus algo to prevent conflicts when multiple nodes are in a network
    def resolve_conflicts(self):
        neighbors = self.nodes
        new_chain = None
        max_length = len(self.chain)

        # check each node to find the longest chain
        for node in neighbors:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        if new_chain:
            self.chain = new_chain
            return True

        return False

    # checks if the hash has 4 leading zeros. returns boolean.
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # the addition of leading zeros can make a massive difference to the time required to find a solution.
        return guess_hash[:4] == "0000"

    # hashes a block
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    # returns the last block of the chain
    @property
    def last_block(self):
        return self.chain[-1]