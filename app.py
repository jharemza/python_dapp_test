from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/595e7fb8bbf04548ab0e847a61d333da"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.block_number())

balance = web3.eth.getBalance("0xa1CFBA7483FAA5372a2FCdD777046ED4b95db966")
print(web3.fromWei(balance, "ether"))