import json
from web3 import Web3, HTTPProvider

class EnergyToken:
    def __init__(self):
        self.w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))
        self.contract_address = '0x...YOUR_CONTRACT_ADDRESS...'
        self.contract_abi = json.load(open('energy_token_abi.json'))

    def deploy_contract(self):
        contract = self.w3.eth.contract(abi=self.contract_abi)
        tx_hash = contract.constructor().transact({'from': '0x...YOUR_WALLET_ADDRESS...'})
        self.w3.eth.waitForTransactionReceipt(tx_hash)

    def mint_tokens(self, amount):
        contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        tx_hash = contract.functions.mint(amount).transact({'from': '0x...YOUR_WALLET_ADDRESS...'})
        self.w3.eth.waitForTransactionReceipt(tx_hash)

    def transfer_tokens(self, from_address, to_address, amount):
        contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        tx_hash = contract.functions.transfer(from_address, to_address, amount).transact({'from': '0x...YOUR_WALLET_ADDRESS...'})
        self.w3.eth.waitForTransactionReceipt(tx_hash)

energy_token = EnergyToken()
