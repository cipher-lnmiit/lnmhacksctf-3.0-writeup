// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoMixer {
    struct Deposit {
        address depositor;
        uint256 amount;
        uint256 blockNumber;
    }

    Deposit[] public deposits;
    mapping(address => uint256) public balances;
    
    event DepositMade(address indexed depositor, uint256 amount, uint256 blockNumber);
    event WithdrawalMade(address indexed recipient, uint256 amount, bytes data);

    function deposit() external payable {
        require(msg.value > 0, "Must deposit something");
        
        deposits.push(Deposit({
            depositor: msg.sender,
            amount: msg.value,
            blockNumber: block.number
        }));
        
        balances[msg.sender] += msg.value;
        
        emit DepositMade(msg.sender, msg.value, block.number);
    }

    function withdraw(address[] calldata recipients, uint256[] calldata amounts, bytes[] calldata dataMessages) external {
        require(recipients.length == amounts.length && amounts.length == dataMessages.length, "Length mismatch");
        
        uint256 totalAmount = 0;
        for(uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }
        
        require(balances[msg.sender] >= totalAmount, "Insufficient balance");
        
        balances[msg.sender] -= totalAmount;
        
        for(uint256 i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(amounts[i]);
            emit WithdrawalMade(recipients[i], amounts[i], dataMessages[i]);
        }
    }

    function getDepositCount() external view returns (uint256) {
        return deposits.length;
    }

    function getDeposit(uint256 index) external view returns (address, uint256, uint256) {
        Deposit memory d = deposits[index];
        return (d.depositor, d.amount, d.blockNumber);
    }

    receive() external payable {
        this.deposit();
    }
}
