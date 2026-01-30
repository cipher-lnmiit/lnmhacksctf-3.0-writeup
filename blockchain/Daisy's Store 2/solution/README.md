# Solution to `Daisy's Store 2`

The contract batches transaction but doesn't verify the batches.
So a contract that submits 2 batches in the same function will execute it before the final states update.
So you can call `buyBatch` twice and get over a 100 items.

Flag: LNMHACKS{b47ch_v3rific47i0n_is_n33d3d}