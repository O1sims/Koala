# Kalua

## Overview

Kalua is a Python-based web application that illustrates the concept of [blockchain](https://en.wikipedia.org/wiki/Blockchain). The application provides a simple website that allows users to store and share information. The information shared on the blockchain is identified by three essential fields: (1) content; (2) author; and (3) timestamp. Because the content will be stored on the blockchain, it is immutable and permanent.

## Technology stack

The Python web application uses [Flask](http://flask.pocoo.org/) as its framework. Since this is just a mini application, there is no separate frontend framework and the blockchain data is just stored in-memory on the node server(s), so no separate database is used.

## Running the application

There are two parts to this application: the node server and the client-side application itself. The node server handles the creation of blocks and the development of the blockchain. The client application handles the submission of transactions.

To start the blockchain node server `cd` into the `Kalua` directory and run the following command:
```
python node_server.py
```
To spin up the client-side application, again make sure that you are in the `Kalua` directory and run:
```
python run_app.py
```
By default, the node server will be running on port `8000` and the client-side application will be running on port `5000`.

To play around by spinning off multiple custom nodes, use the `add_nodes/` endpoint to register a new node. To update the node with which the application syncs, change `CONNECTED_NODE_ADDRESS` field in the `views.py` file.

## Contact

The best way to troubleshoot or ask for a new feature or enhancement is to create a Github [issue](https://github.com/O1sims/Kalua/issues). However, if you have any further questions you can contact [me](mailto:sims.owen@gmail.com) directly.
