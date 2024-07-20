class P2PTrading:
    def __init__(self):
        self.trades = []

    def create_trade(self, buyer, seller, energy_amount):
        # create a new trade between two parties
        self.trades.append((buyer, seller, energy_amount))

    def get_trades(self):
        return self.trades
