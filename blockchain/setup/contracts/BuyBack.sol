// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract BuyBack {
    mapping(address => uint256) public balances;
    mapping(address => uint256) public items;
    mapping(address => bool) public initialised;

    string flag = "LNMHACKS{y0u_g0t_f0r_fr33!!!}";

    error InsufficientBalance(uint256 currentBalance, uint256 requiredBalance);
    error InsufficientItems(uint256 currentItems, uint256 requiredItems);

    modifier isInitialised() {
        require(initialised[msg.sender] == true);
        _;
    }

    function initialise() public payable {
        initialised[msg.sender] = true;
        balances[msg.sender] = 100;
        items[msg.sender] = 0;
    }

    function buy(uint256 amount) public payable isInitialised {
        if(amount > balances[msg.sender]){
            revert InsufficientBalance(balances[msg.sender], amount);
        }

        items[msg.sender] += amount;
        
        // Just checking if they are real :/
        (bool success, ) = msg.sender.call{value: 0}("");
        require(success, "Callback failed");
        
        // Don't want to stop people who love my products :))
        unchecked {
            balances[msg.sender] -= amount;
        }
    }

    function sell(uint256 amount) public isInitialised {
        if(amount > items[msg.sender]){
            revert InsufficientItems(items[msg.sender], amount);
        }

        balances[msg.sender] += amount;
        items[msg.sender] -= amount;
    }

    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }

    function getFlag() public view isInitialised returns (string memory){
        if(items[msg.sender] > 100){
            return flag;
        }
        return "";
    }

    // Who doesn't like free money !!
    receive() external payable {}
}