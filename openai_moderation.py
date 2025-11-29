import base64
from openai import OpenAI
from tkinter import Tk, Text, Label, Button, filedialog, messagebox

client = OpenAI(api_key="YOUR_API_KEY")

image_base64 = None

def browse_image():
    global image_base64, selected_image_path
    selected_image_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
    
    if selected_image_path:
        with open(selected_image_path, "rb") as img_file:
            b64 = base64.b64encode(img_file.read()).decode("utf-8")
            image_base64 = f"data:image/jpeg;base64,{b64}"
        img_label.config(text=f"Selected Image: {selected_image_path.split('/')[-1]}")
    else:
        img_label.config(text="No image selected")

def moderate():
    caption = text_input.get("1.0", "end").strip()

    if not image_base64 and not caption:
        messagebox.showerror("Error", "Add an image or caption first.")
        return

    inputs = []
    if caption:
        inputs.append({"type": "text", "text": caption})
    if image_base64:
        inputs.append({"type": "image_url", "image_url": {"url": image_base64}})

    try:
        response = client.moderations.create(
            model="omni-moderation-latest",
            input=inputs
        )

        result = response.results[0]

        scores = result.category_scores.model_dump()

        output = f"Flagged: {result.flagged}\n\nCategory Scores:\n"
        for cat, val in scores.items():
            output += f"{cat}: {val:.3f}\n"

        messagebox.showinfo("Moderation Results", output)


    except Exception as e:
        messagebox.showerror("Error", str(e))


# UI Setup
root = Tk()
root.title("OpenAI Multi-Modal Moderation Tester")
root.geometry("450x400")

Label(root, text="Upload an Image:").pack(pady=5)
Button(root, text="Browse", command=browse_image).pack()
img_label = Label(root, text="No image selected", fg="gray")
img_label.pack()

Label(root, text="Enter Caption:").pack(pady=10)
text_input = Text(root, height=7, width=50)
text_input.pack()

Button(root, text="Analyze Moderation", command=moderate,
       bg="black", fg="white").pack(pady=20)

root.mainloop()
