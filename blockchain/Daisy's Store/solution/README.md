# Solution to `Connect to the chain`

The `BuyBack.sol` contract has a re-entrancy vulnerability which can be exploited by buying again before the state has been finalised.
A sample exploit contract `AttackBuyBack.sol` has been given which can be deployed and the `attack` function can be called.