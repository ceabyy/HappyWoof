import torch
import torchvision
from torchvision import datasets, transforms, models
from torch.utils.data import random_split
import torch.nn as nn

# for mac gpu to be used
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")


# MODEL

# transforms

train_transforms = transforms.Compose ([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.3),
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# split data into sets

fullDataset = datasets.ImageFolder("./data", transform=train_transforms)

trainSize = int(0.8*len(fullDataset))
valSize = int(0.1*len(fullDataset))
testSize = len(fullDataset) - trainSize - valSize

trainData, valData, testData = random_split(fullDataset, [trainSize, valSize, testSize])

train_loader = torch.utils.data.DataLoader(trainData, batch_size=32, shuffle=True)
val_loader = torch.utils.data.DataLoader(valData, batch_size=32) 

# use a pretrained model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.fc = nn.Linear(model.fc.in_features, 4) # angry, happy, relaxed, sad
model = model.to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# train and validation

for epoch in range(100):

    print(f"Epoch {epoch+1}/10 starting...")

    # training
    model.train()
    train_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    # validation
    model.eval()
    val_loss = 0  
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item() 
            _, predicted = torch.max(outputs.data, 1)           
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    val_accuracy = 100 * (correct/total)

    print(f"Epoch {epoch+1}, Train Loss: {train_loss/len(train_loader):.4f}, Val Loss: {val_loss/len(val_loader):.4f}, Val Accuracy: {val_accuracy:.4f}%")

torch.save(model.state_dict(), "dog_mood_model.pth")
print("Model saved!")