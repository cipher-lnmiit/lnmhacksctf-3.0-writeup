import torch
import torch.nn as nn

# The Flag
flag = "LNMHACKS{LOG1T}"

# Storage for model parameters
state_dict = {}

for i, char in enumerate(flag):
    target_x = ord(char)
    
    # We want mx + b = 0 when x = target_x
    # Let's pick a simple m=1 for simplicity, so b = -target_x
    m = 1.0
    b = -float(target_x)
    
    # Store them with unique keys for each character 'node'
    state_dict[f"char_{i}.weight"] = torch.tensor([[m]])
    state_dict[f"char_{i}.bias"] = torch.tensor([b])

torch.save(state_dict, "logistic_challenge.pth")
print(f"Challenge created with {len(flag)} characters.")