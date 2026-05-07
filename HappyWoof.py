import torch
import torchvision
from torchvision import datasets, transforms, models
from torch.utils.data import random_split
import torch.nn as nn
from PIL import Image
import torch.nn.functional as F

# to communicate with js
from flask import Flask, jsonify, request
app = Flask(__name__)

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

classes = ["angry", "happy", "relaxed", "sad"]

model = models.resnet18(weights=None) # function does the prediction
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


@app.route('/predictDog', methods=['POST']) # for flask
def predictDog(): #using file from page

    """ # since the image is given through html file
    Tk().withdraw()
    file_path = filedialog.askopenfilename()
    """
    file = request.files['image']
    image = Image.open(file).convert("RGB")
    image = train_transforms(image).unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image)
        probabilities = F.softmax(outputs, dim=1)

        _, predicted = torch.max(outputs, 1)

    for i, prob in enumerate(probabilities[0]):
        print(f"{classes[i]}: {prob.item() * 100:.2f}%")

    print(f"Your dog seems to be {classes[predicted.item()]}!")

    result = {classes[i]: round(probabilities[0][i].item() * 100, 2) for i in range(len(classes))}
    result["prediction"] = classes[predicted.item()]

    return jsonify(result)

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))