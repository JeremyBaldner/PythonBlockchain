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
* Contains routes for creating transactions, mining, viewing the full chain,<br>registering nodes, and resolving consensus 
issues.

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
body: { "nodes" : [ "http://127.0.0.1:5001" ] } &emsp;  <-- note: You will need another server running on port 5001 to run the next request. 
* GET: http://localhost:5001/mine
* GET: http://localhost:5000/nodes/resolve
