import json
import datetime
import requests

from app import app
from flask import render_template, redirect, request


# The node with which our application interacts
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []


def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    response = requests.get(
        url="{}/chain".format(
            CONNECTED_NODE_ADDRESS))
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)
        global posts
        posts = sorted(
            content,
            key=lambda k: k['timestamp'],
            reverse=True)


@app.route('/')
def index():
    fetch_posts()
    return render_template(
        'index.html',
        title='Kalua: Decentralized messaging',
        posts=posts,
        node_address=CONNECTED_NODE_ADDRESS,
        readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    author = request.form["author"]
    post_object = {
        'author': author,
        'content': post_content,
    }
    # Submit a transaction
    requests.post(
        url="{}/new_transaction".format(
            CONNECTED_NODE_ADDRESS),
        json=post_object,
        headers={'Content-type': 'application/json'})
    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
