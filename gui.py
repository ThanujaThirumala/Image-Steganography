import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import encode_image, decode_image
from PIL import Image, ImageTk

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")

        # Heading
        tk.Label(self.root, text="Image Steganography", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Image selection
        self.image_path = ""
        tk.Button(self.root, text="Choose Image", command=self.select_image).pack(pady=5)
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Message input
        self.message_entry = tk.Text(root, height=5, width=40)
        self.message_entry.pack(pady=10)

        # Encode & decode buttons
        tk.Button(root, text="Encode & Save", command=self.encode).pack(pady=5)
        tk.Button(root, text="Decode Message", command=self.decode).pack(pady=5)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((300, 300))
            self.tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_img)

    def encode(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Error", "Please enter a message to encode.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            try:
                encode_image(self.image_path, save_path, message)
                messagebox.showinfo("Success", f"Message encoded and saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def decode(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return
        try:
            message = decode_image(self.image_path)
            messagebox.showinfo("Hidden Message", message)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()