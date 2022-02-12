from encodings import utf_8
from web3 import Web3

ganache_url = 'https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0xD3bd6D866f9e421e2E28A7275116B5796fB401f3'
private_key1 = 'my prv key'
account_2 = '0xc53D6C0148ddC28Efe623Ab3aD54da5C7779b25C'
nonce = web3.eth.getTransactionCount(account_1)
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'data': bytes("Hvozdak_Viktoriia", "utf_8")
}
signed_tx = web3.eth.account.sign_transaction(tx, private_key1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
