import torch

def solve_multi_layer_challenge(file_path):
    # Load the state dict
    state_dict = torch.load(file_path, weights_only=True, map_location='cpu')
    
    # Target the specific layer you created
    target_key = 'layer3.bias'
    
    if target_key not in state_dict:
        print(f"Target {target_key} not found. Available biases:")
        print([k for k in state_dict.keys() if 'bias' in k])
        return None

    biases = state_dict[target_key]
    
    # Convert to list and characters
    # Using .tolist() avoids the NumPy dependency warning 
    flag_chars = []
    for val in biases.tolist():
        # Ensure the value is a valid ASCII range
        if 32 <= int(round(val)) <= 126:
            flag_chars.append(chr(int(round(val))))
        else:
            flag_chars.append('?') # Placeholder for non-printable noise

    return "".join(flag_chars)

if __name__ == "__main__":
    model_path = 'challenge.pth'
    flag = solve_multi_layer_challenge(model_path)
    if flag:
        print(f"Extracted Flag from 'vuln.bias': {flag}")