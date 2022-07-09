import os
import json
from web3 import Web3, HTTPProvider
#infura eth node setup
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/23af3641125944e19af2086ae387fe3b"))
connection = w3.isConnected()
#setup addresses and privatekey
owner = Web3.toChecksumAddress('add1')
reciever = Web3.toChecksumAddress('add2')
privateKey = 'PRIVATE_KEY'

#amount of transactions on owner's address
nonce = w3.eth.getTransactionCount(owner)
#transaction object
tx = {
    'nonce': nonce,
    'to': reciever,
    'value': w3.toWei(0.001, 'ether'),
    'gas': 21000,
    'gasPrice': w3.toWei('40', 'gwei'),
}
#sign transaction with privatekey from owner
signedTx = w3.eth.account.signTransaction(tx,privateKey)
#send raw transaction to eth node
txHash = w3.eth.sendRawTransaction(signedTx.rawTransaction)