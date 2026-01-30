# Solution to `Trace-able transaction`

The crypto mixer does mix transaction but if there is only one person in a single block, it will distribute funds only for that one person and thus the person will get traced.
Just look for the transaction history of the crypto mixer and find the block where there is only one in-bound transaction.
Look at the wallets it was distributed to and the message will have the flags in parts.

Flag: LNMHACKS{tr4ck3d_thr0ugh_s1ngl3_bl0ck_d3p0s1t}