import torch
import torch.nn as nn
import torch.optim as optim
import time
import pyautogui
import random

from actions import *
from readStats import *

# ----------------------------
# paramètres
# ----------------------------
state_size = 18
action_size = 5 # nombre d'actions possibles

# ----------------------------
# fonctions de lecture d'état
# ----------------------------
def read_state():
    global step, building_count

    money = read_money()
    population = read_population()
    satisfaction = read_satisfaction()
    happinness = read_happinness()

    political = read_political()

    housing = read_housing()
    food = read_food()
    industry = read_industry()
    tourism = read_tourism()

    return [
        money,
        population,
        satisfaction,
        happinness,
        *political,
        housing,
        food,
        industry,
        tourism,
        step,
        building_count
    ]

# ----------------------------
# fonctions d'action
# ----------------------------
def perform_action(action):
    global building_count

    if action == 0:
        build_something()
        building_count += 1

    elif action == 1:
        click_on_map()

    elif action == 2:
        random_scroll()

    elif action == 3:
        pyautogui.click(966, 838)

    elif action == 4:
        pyautogui.click(971, 891)
        time.sleep(5)
        pyautogui.click(850, 600)


def encode_action(action, action_size):
    vec = [0]*action_size
    vec[action] = 1
    return vec

def choose_action():
    return torch.randint(0, action_size, (1,)).item()

# ----------------------------
# création dataset
# ----------------------------
dataset = []

step = 0
building_count = 0

n_samples = 5000  # ajuster selon la durée que tu peux consacrer

for i in range(n_samples):
    state = read_state()
    action = choose_action()
    perform_action(action)
    time.sleep(5)
    next_state = read_state()

    dataset.append({
        "state": state,
        "action": encode_action(action, action_size),
        "next_state": next_state
    })

    step += 1
    print("sample", i)

torch.save(dataset,"dataset_tropico.pt")
# ----------------------------
# préparation des données
# ----------------------------
states = torch.tensor([d["state"] for d in dataset], dtype=torch.float32)
actions = torch.tensor([d["action"] for d in dataset], dtype=torch.float32)
next_states = torch.tensor([d["next_state"] for d in dataset], dtype=torch.float32)

# normalisation
max_vals = states.max(dim=0)[0]
states = states / max_vals
next_states = next_states / max_vals

# ----------------------------
# modèle
# ----------------------------
class WorldModel(nn.Module):

    def __init__(self,state_size,action_size):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(state_size+action_size,256),
            nn.ReLU(),

            nn.Linear(256,256),
            nn.ReLU(),

            nn.Linear(256,state_size)
        )

    def forward(self,state,action):

        x = torch.cat((state,action),dim=1)

        return self.net(x)

# ----------------------------
# entraînement
# ----------------------------
model = WorldModel(state_size,action_size)
optimizer = optim.Adam(model.parameters(),lr=0.001)
loss_fn = nn.MSELoss()

epochs = 200

for epoch in range(epochs):

    pred = model(states,actions)

    loss = loss_fn(pred,next_states)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print("epoch",epoch,"loss",loss.item())

torch.save(model.state_dict(),"tropico_world_model.pth")

# ----------------------------
# test du modèle
# ----------------------------
test_state = torch.tensor([read_state()], dtype=torch.float32) / max_vals
test_action = torch.tensor([encode_action(1, action_size)], dtype=torch.float32)
prediction = model(test_state, test_action)
print("predicted next state:", prediction.detach().numpy() * max_vals.numpy())

i = random.randint(0, len(states)-1)

state = states[i].unsqueeze(0)
action = actions[i].unsqueeze(0)
true_next = next_states[i]

pred = model(state, action).detach()

print("true:", true_next * max_vals)
print("pred:", pred.squeeze() * max_vals)

torch.save(model.state_dict(), "tropico_world_model.pth")