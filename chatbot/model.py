import torch
import torch.nn as nn

# Create a class called NeuralNetwork (can be any name) derived from nn.Module
class NeuralNetwork(nn.Module):
    # Define the init which gets self
    def __init__(self, input_size, hidden_size, num_classes): # This will be a feed forward neural net with 2 hidden layers
        super(NeuralNetwork, self).__init__()
        # Create 3 linear layers - input_size and num_classes must be fixed but the hidden layer's sizes (hidden_size) can vary
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        # Create an activation function in between
        self.relu = nn.ReLU()

    # implement the forward path
    def forward(self, x):
        # Passing the output from each linear layer to the next
        # Linear layer 1
        out = self.l1(x) # Gets x as input first
        out = self.relu(out)    # Apply activation funciton in between, this gets x from above
        # Linear layer 2
        out = self.l2(out) # Previous output of linear layer 1 as input
        out = self.relu(out)    # Apply activation funciton in between, this uses the output from above as the input
        # Linear layer 3
        out = self.l3(out) # Previous output of linear layer 2 as input
        # No activation function and no softmax for linear layer 3 since later when we apply the CrossEntropyLoss, it will already automatically apply to linear layer 3 as well
        return out # Return the output

