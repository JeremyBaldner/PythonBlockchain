# Python Blockchain
### A simple blockchain setup using python. This blockchain utilizes the PoW and consensus algorithms. 

This project was created by following Daniel van Flymen's guide on 
<a href="https://hackernoon.com/learn-blockchains-by-building-one-117428612f46">Learn Blockchains by Building One</a>. 
This project contains two simple files to run the application on localhost for basic understanding and testing. For
this project I utilized PyCharm and with the python interpreter 3.11.

#### Try it out:
* clone or fork this project
* Run the app.py file on your favorite IDE or from the CLI with "python app.py"

#### The app file:
* Starts the server on a localhost port
* Connects to the blockchain
* Contains routes for creating transactions, mining, viewing the full chain,<br>registering nodes, and resolving 
consensus issues.

#### The blockchain file:
* Initializes the blockchain and node
* Contains the Proof of Work and Consensus algorithms
* Creates new transactions, routes, and validation
* Performs Block Hashing with the Secure Hash Algorithm 256-bit

#### Test with Postman requests:
* POST: http://localhost:5000/transactions/new <br>
body: { "sender" : "d4ee26eee15148ee92c6cd394edd974e", "recipient" : "a different address", "amount" : "5" }
* GET: http://localhost:5000/mine
* GET: http://localhost:5000/chain
* POST: http://localhost:5000/nodes/register <br>
body: { "nodes" : [ "http://127.0.0.1:5001" ] } &emsp;  <-- note: You will need another server running on port 5001 to 
run the next request. 
* GET: http://localhost:5001/mine
* GET: http://localhost:5000/nodes/resolve

## Purpose
Blockchains are created to eliminate the need for third parties, like banks, to complete secure digital transactions. 
New blocks in the chain are verified by miners and miners are rewarded with a digital “coin”. These coins now hold 
monetary value which can be traded for goods and services.

## Blockchain vs Linked-List
When learning about blockchains and their pointers and nodes, it can be hard to not immediately think about a 
linked-list. While the concepts are similar, there are a few key differences between them. Blockchains are immutable 
since they do not contain the function for modifying the list like a linked-list would. Blockchains point to the 
previous block whereas linked-list point to the next memory location. Blockchains also contain a function to verify 
a block prior to appending to the chain.

## Storage
Blockchains are saved on a “shared database” but what does this mean? Blockchains contain nodes that represent the 
different IoT devices connected to them. Each node holds and updates the chain (ledger) with each block and it's 
transactions when connected. This makes it “decentralized” compared to holding the data on one single (central) server. 
This means mass adoption is mandatory to maintain a continuous connection to the blockchain. If all nodes are turned 
off, the blockchain would cease to exist. <br><br>
Since the blockchain nodes must contain the full ledger, storage size could become an issue. The current common storage 
compacity is 1-6TB. As the ledger grows, storage capacity will need to match it. This will also prove to be an issue 
for new nodes that must first download the entire ledger before mining.