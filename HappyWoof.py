import torch
import torchvision
from torchvision import datasets, transforms, models
from torch.utils.data import random_split
import torch.nn as nn
from PIL import Image
from tkinter import Tk, filedialog
import torch.nn.functional as F

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

print("Welcome to HappyWoof! Let's find out how your furry friend is doing today.")
print("Please upload an image of your pet to get started:")

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 4)

model.load_state_dict(torch.load("./dog_mood_model_100.pth", map_location=device))
model = model.to(device)
model.eval()

train_transforms = transforms.Compose ([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.3),
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

Tk().withdraw()
file_path = filedialog.askopenfilename()

image = Image.open(file_path).convert("RGB")
image = train_transforms(image).unsqueeze(0).to(device)

with torch.no_grad():

    outputs = model(image)
    probabilities = F.softmax(outputs, dim=1)

    _, predicted = torch.max(outputs, 1)


classes = ["angry", "happy", "relaxed", "sad"]

for i, prob in enumerate(probabilities[0]):
    print(f"{classes[i]}: {prob.item() * 100:.2f}%")

print(f"Your pet seems to be {classes[predicted.item()]}!")