import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms

# CNN simple pour 0-9
class DigitNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, 1)
        self.conv2 = nn.Conv2d(16, 32, 3, 1)
        self.fc1 = nn.Linear(32*5*5, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

digit_model = DigitNet()
digit_model.load_state_dict(torch.load("digit_model.pt"))  # ton modèle pré-entraîné
digit_model.eval()

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28,28)),
    transforms.ToTensor()
])

def read_number(img):
    img_t = transform(img).unsqueeze(0)  # ajouter batch dim
    with torch.no_grad():
        output = digit_model(img_t)
        return output.argmax(dim=1).item()