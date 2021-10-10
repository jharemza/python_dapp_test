from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Test connection to block chain
# print(web3.isConnected())

account_1 = "0x0f69191310Cd12A11B3C6E7713FA822F89fe6984"
account_2 = "0x96E9E21C9C2Fd83B940C61f64b9828Af1d8587Fb"

private_key = "bdca9648dae0fd7fdc97835f8126be9319314e9dad101a0f430659e0b38c9476"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)

# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send a transaction
# get transaction hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))