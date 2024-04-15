import torch
import pandas as pd
import numpy as np
from pathlib import Path
from model import SpamClf
from transformers import BertModel, BertTokenizer
from web3 import Web3
import json
from utils import *
import time

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# load trained model
save_dir = f"models/"
model_name = "bert-base-uncased"
bert_tokenizer = BertTokenizer.from_pretrained(model_name)
bert_model = BertModel.from_pretrained(model_name)
spam_clf = SpamClf(bert_model)
spam_clf.load_state_dict(torch.load(f"{save_dir}/pytorch_model.bin"))
spam_clf.eval()

# connent to eth
infura_url = "https://sepolia.infura.io/v3/29be0acae77c4f56af14e72df9b99dc1"
w3 = Web3(Web3.HTTPProvider(infura_url))

# contract address, ABI and private key
contract_abi = json.load(open("abi.json"))
contract_address = "0x77712B21de953544a11f8825cC485bf8e1197e79"
PRIVATE_KEY = "b86b4e07800868d04de104582677760fcbffe8461e6481968c3b60ef802620a1"

# creat contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)


# def process_input_msg(input_msg):
def process_input_msg():

    # retrieve msg from contract
    input_msg = contract.functions.getInputData().call()
    input_msg = str(input_msg)
    print(f"input_msg: {input_msg}")

    # tokenization
    msg_tokens = tokenize_function([input_msg], model_name)

    # input msg to ML model
    preds = spam_clf(msg_tokens)
    preds = torch.argmax(preds, dim=1)
    output = "ham" if preds == 0 else "spam"
    print(f"ML output: {output}")

    # send result back to blockchain (contract)
    tx = contract.functions.setOutputData(output).build_transaction(
        {
            "from": "0x1157930a546a0312624204D49db8C291fC71047A",  # eth account address
            "gas": 300000,  # gas limitation
            "gasPrice": w3.to_wei("50", "gwei"),  # gas price
            "nonce": w3.eth.get_transaction_count(
                "0x1157930a546a0312624204D49db8C291fC71047A"
            ),  # use account address to retrieve nonce
        }
    )
    signed_tx = w3.eth.account.sign_transaction(
        tx, private_key=PRIVATE_KEY
    )  # use private key to prove
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)  # send transaction
    print(tx_hash)

    return tx_hash


# def getOutput():
#     output = contract.functions.getInputData().call()
#     print(output)
#     if output == None or output == "None":
#         return "pending"
#     else:
#         tx = contract.functions.setOutputData("None").build_transaction(
#             {
#                 "from": "0x1157930a546a0312624204D49db8C291fC71047A",  # eth account address
#                 "gas": 300000,  # gas limitation
#                 "gasPrice": w3.to_wei("50", "gwei"),  # gas price
#                 "nonce": w3.eth.get_transaction_count(
#                     "0x1157930a546a0312624204D49db8C291fC71047A"
#                 ),  # use account address to retrieve nonce
#             }
#         )
#         signed_tx = w3.eth.account.sign_transaction(
#             tx, private_key=PRIVATE_KEY
#         )  # use private key to prove
#         w3.eth.send_raw_transaction(signed_tx.rawTransaction)
#         time.sleep(10)
#         return output


def getOutput():
    time.sleep(5)
    output = contract.functions.getInputData().call()
    return output
