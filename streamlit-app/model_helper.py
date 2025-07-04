import os
from PIL import Image
import torch
import torch.nn as nn
from torchvision import models, transforms

trained_model = None
class_names = ['Front Breakage', 'Front Crushed', 'Front Normal',
               'Rear Breakage', 'Rear Crushed', 'Rear Normal']

class car_damage_detection(nn.Module):
    def __init__(self, num_classes=6):
        super().__init__()
        self.model = models.resnet50(weights='DEFAULT')

        # Freeze all layers
        for param in self.model.parameters():
            param.requires_grad = False

        # Unfreeze last block and fc layers
        for param in self.model.layer4.parameters():
            param.requires_grad = True

        self.model.fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(self.model.fc.in_features, num_classes)
        )

    def forward(self, x):
        return self.model(x)

def predict(image_path):
    image = Image.open(image_path).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    global trained_model
    if trained_model is None:
        trained_model = car_damage_detection()

        # ✅ Correct model path relative to model_helper.py
        current_dir = os.path.dirname(__file__)
        model_path = os.path.abspath(os.path.join(current_dir, 'model', 'saved_model.pth'))

        # Safety check
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")

        print(f"[INFO] Loading model from: {model_path}")
        trained_model.load_state_dict(torch.load(model_path, map_location='cpu'))
        trained_model.eval()

    with torch.no_grad():
        output = trained_model(image_tensor)
        _, predicted_class = torch.max(output, 1)
        return class_names[predicted_class.item()]
