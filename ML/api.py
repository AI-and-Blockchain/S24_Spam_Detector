from flask import Flask, request, jsonify
from celery import Celery
from contract_interface import *  # Importing the contract interaction module

app = Flask(__name__)


# @celery.task(bind=True)
def process_transaction():
    # # Simulate interacting with the smart contract
    # contract_output = contract_interface.interact_with_contract(message)
    # # Assuming a function `process_with_ml_model` exists within contract_interface.py
    # ml_result = contract_interface.process_with_ml_model(contract_output)
    # # Sending result back to the smart contract
    hash = process_input_msg()
    return hash


@app.route("/api/start_transaction", methods=["POST"])
def start_transaction():
    print(request.data)
    data = request.get_json()
    msg = data.get("message")
    if msg is not None:
        hash = process_transaction()
    return jsonify({"status": "Processing", "task_id": str(hash)}), 202


@app.route("/api/output", methods=["GET"])
def output():
    output = getOutput()
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
