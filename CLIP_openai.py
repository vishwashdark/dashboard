import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import torch
import open_clip
from PIL import Image
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model at startup
print("Loading OpenCLIP model… please wait (this may take ~20–40 sec on CPU)")
model_name = "ViT-L-14"
pretrained = "laion2b_s32b_b79k"
model, _, preprocess = open_clip.create_model_and_transforms(
    model_name, pretrained=pretrained
)
tokenizer = open_clip.get_tokenizer(model_name)
model = model.to(device)
model.eval()
torch.set_grad_enabled(False)
print("Model loaded successfully!")


selected_image_path = None


def browse_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.jfif;*.webp")]
    )
    if selected_image_path:
        img_label.config(text=f"Selected: {os.path.basename(selected_image_path)}")
    else:
        img_label.config(text="No image selected")


def run_similarity():
    if not selected_image_path:
        messagebox.showerror("Error", "Please select an image")
        return

    caption = text_box.get("1.0", tk.END).strip()
    if not caption:
        messagebox.showerror("Error", "Please enter a caption")
        return

    # Process image + caption
    image = preprocess(Image.open(selected_image_path)).unsqueeze(0).to(device)
    text = tokenizer([caption]).to(device)

    with torch.no_grad():
        img_feat = model.encode_image(image)
        txt_feat = model.encode_text(text)

    img_feat /= img_feat.norm(dim=-1, keepdim=True)
    txt_feat /= txt_feat.norm(dim=-1, keepdim=True)

    similarity = (img_feat @ txt_feat.T).item()

    # Interpretation
    if similarity > 0.35:
        meaning = "Aligned — Caption matches the image"
    elif similarity >= 0.20:
        meaning = "Unclear/Vague — Social caption but not misleading"
    else:
        meaning = "Potentially Misleading — Caption image mismatch"

    message = f"Similarity Score: {similarity:.3f}\n\nAssessment:\n{meaning}"
    messagebox.showinfo("CLIP Analysis Result", message)


def analyze():
    threading.Thread(target=run_similarity).start()


# Build UI
root = tk.Tk()
root.title("OpenCLIP Misleading Content Detector")
root.geometry("520x430")

tk.Label(root, text="Upload an Instagram Post Image:").pack(pady=6)
tk.Button(root, text="Browse Image", command=browse_image).pack()
img_label = tk.Label(root, text="No image selected", fg="gray")
img_label.pack()

tk.Label(root, text="Enter Caption:").pack(pady=10)
text_box = tk.Text(root, height=6, width=55)
text_box.pack()

tk.Button(root, text="Analyze Post", bg="black", fg="white", command=analyze).pack(pady=20)

root.mainloop()
