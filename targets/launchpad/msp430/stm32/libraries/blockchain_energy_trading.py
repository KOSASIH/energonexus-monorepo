import hashlib

class BlockchainEnergyTrading:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def add_block(self, block):
        self.chain.append(block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        # mine a new block and add it to the chain
        pass

    def get_chain(self):
        return self.chain

    def get_pending_transactions(self):
        return self.pending_transactions
