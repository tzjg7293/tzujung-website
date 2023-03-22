import torch
import torch.nn as nn

# Create a class called NeuralNetwork (can be any name) derived from nn.Module
class NeuralNetwork(nn.Module):
    # Define the innit which gets self
    def __init__(self, input_size, hidden_size, num_classes): # This will be a feed forward neural net with 2 hidden layers
       
        # Create 3 linear layers - input_size and num_classes must be fixed but the hidden layer's sizes (hidden_size) can vary
        self.l1 = nn.linear(input_size, hidden_size)
        self.l2 = nn.linear(hidden_size, hidden_size)
        self.l3 = nn.linear(hidden_size, num_classes)

