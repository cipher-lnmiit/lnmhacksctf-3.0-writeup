import torch

def solve():
    # Load the parameters
    data = torch.load("logistic_challenge.pth", weights_only=True)
    
    # We need to know how many characters there are. 
    # We can count the 'bias' keys.
    num_chars = len([k for k in data.keys() if "bias" in k])
    
    flag = []
    
    for i in range(num_chars):
        m = data[f"char_{i}.weight"].item()
        b = data[f"char_{i}.bias"].item()
        
        # Solve for x: mx + b = 0  => x = -b / m
        threshold = -b / m
        
        # Round to nearest integer and convert to ASCII
        flag.append(chr(int(round(threshold))))
        
    return "".join(flag)

if __name__ == "__main__":
    print(f"Recovered Flag: {solve()}")