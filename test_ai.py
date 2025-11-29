import torch
from torchvision import transforms
from PIL import Image
import torch.nn as nn
from torchvision.models import mobilenet_v2


def load_model(weights_path):
    print("Loading model...")

    # Create architecture
    model = mobilenet_v2(weights=None)
    model.classifier[1] = nn.Linear(model.last_channel, 2)  # 2 classes: real / fake

    # Load checkpoint safely
    checkpoint = torch.load(weights_path, map_location="cpu")
    model.load_state_dict(checkpoint["model_state_dict"])

    model.eval()
    print("Model loaded successfully!")
    return model


def predict_image(model, img_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    img = Image.open(img_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)
        prob = torch.softmax(output, dim=1)[0]

    labels = ["Real", "AI-Generated"]
    idx = int(prob.argmax())
    confidence = float(prob[idx] * 100)

    return labels[idx], confidence


if __name__ == "__main__":
    model = load_model("best_model.pth")

    img_path = input("Enter image filename: ")
    label, score = predict_image(model, img_path)

    print("\n======================")
    print(f"🧠 Prediction: {label}")
    print(f"📈 Confidence: {score:.2f}%")
    print("======================")
