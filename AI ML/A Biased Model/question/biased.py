import torch
import torch.nn as nn

# The Flag
flag = "LNMHACKS{B1AS_IS_B4SED}" 

# Create a simple model
class ChallengeModel(nn.Module):
    def __init__(self):
        super(ChallengeModel, self).__init__()
        # 16 characters in the flag, so we use a layer with 16 outputs
        self.layer1 = nn.Linear(10, len(flag))
        self.layer2 = nn.Linear(len(flag), len(flag))
        self.layer3 = nn.Linear(len(flag), len(flag))
        self.layer4 = nn.Linear(len(flag), len(flag))
        self.layer5 = nn.Linear(len(flag), len(flag))
        self.layer6 = nn.Linear(len(flag), len(flag))

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = self.layer6(x)

model = ChallengeModel()

# Convert flag characters to floats and "poison" the biases
with torch.no_grad():
    for i, char in enumerate(flag):
        # We store the ASCII value as the bias
        model.layer3.bias[i] = ord(char) 

# Save only the state_dict (weights/biases)
torch.save(model.state_dict(), 'challenge.pth')
print("Model 'challenge.pth' created successfully!")