// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

contract OrderShop {
    mapping(address => uint256) public balance;
    mapping(address => uint256) public items;
    mapping(address => mapping(uint256 => bool)) public orderUsed;
    mapping(address => bool) public claimed;

    event Claimed(address indexed user);
    event OrderExecuted(address indexed user, uint256 orderId, uint256 total);

    modifier onlyOnce() {
        require(!claimed[msg.sender], "Already claimed");
        _;
    }

    function claim() external onlyOnce {
        claimed[msg.sender] = true;
        balance[msg.sender] = 100;
        emit Claimed(msg.sender);
    }

    function buyBatch(uint256 orderId, uint256[] calldata quantities) external {
        require(claimed[msg.sender], "Claim first");
        require(!orderUsed[msg.sender][orderId], "Order already used");

        uint256 totalCost = 0;
        for (uint256 i = 0; i < quantities.length; i++) {
            totalCost += quantities[i];
        }

        require(balance[msg.sender] >= totalCost, "Insufficient balance");

        for (uint256 i = 0; i < quantities.length; i++) {
            items[msg.sender] += quantities[i];
        }

        balance[msg.sender] -= totalCost;

        orderUsed[msg.sender][orderId] = true;

        emit OrderExecuted(msg.sender, orderId, totalCost);
    }

    function getFlag() external view returns (string memory) {
        require(items[msg.sender] > 100, "Not enough items");
        return "LNMHACKS{b47ch_v3rific47i0n_is_n33d3d}";
    }
}
