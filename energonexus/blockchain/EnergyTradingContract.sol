pragma solidity ^0.8.0;

contract EnergyTradingContract {
    address private owner;
    mapping (address => uint256) public energyBalances;
    mapping (address => mapping (address => uint256)) public energyTransactions;

    constructor() public {
        owner = msg.sender;
    }

    function buyEnergy(address seller, uint256 amount) public {
        require(energyBalances[seller] >= amount, "Seller does not have enough energy");
        energyBalances[msg.sender] += amount;
        energyBalances[seller] -= amount;
        energyTransactions[msg.sender][seller] += amount;
    }

    function sellEnergy(address buyer, uint256 amount) public {
        require(energyBalances[msg.sender] >= amount, "You do not have enough energy");
        energyBalances[buyer] += amount;
        energyBalances[msg.sender] -= amount;
        energyTransactions[buyer][msg.sender] += amount;
    }

    function getEnergyBalance(address user) public view returns (uint256) {
        return energyBalances[user];
    }

    function getEnergyTransactions(address user) public view returns (uint256[] memory) {
        uint256[] memory transactions = new uint256[](energyTransactions[user].length);
        for (uint256 i = 0; i < energyTransactions[user].length; i++) {
            transactions[i] = energyTransactions[user][i];
        }
        return transactions;
    }
}
