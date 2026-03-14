import torch
import torch.nn as nn
import torch.optim as optim

dataset = torch.load("dataset_tropico.pt")

states = torch.tensor([d["state"] for d in dataset], dtype=torch.float32)
actions = torch.tensor([d["action"] for d in dataset], dtype=torch.float32)
next_states = torch.tensor([d["next_state"] for d in dataset], dtype=torch.float32)

max_vals = states.max(dim=0)[0]

states = states / max_vals
next_states = next_states / max_vals