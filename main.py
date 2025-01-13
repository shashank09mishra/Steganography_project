import tkinter as tk
from tkinter import filedialog, messagebox
from encode import encode_message
from decode import decode_message

def open_encode_window():
    encode_window = tk.Toplevel(root)
    encode_window.title("Encode Message")

    tk.Label(encode_window, text="Select Image File:").pack(pady=5)
    image_path_entry = tk.Entry(encode_window, width=40)
    image_path_entry.pack(pady=5)

    def select_image():
        image_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, image_path)

    tk.Button(encode_window, text="Browse", command=select_image).pack(pady=5)

    tk.Label(encode_window, text="Enter Message:").pack(pady=5)
    message_entry = tk.Entry(encode_window, width=40)
    message_entry.pack(pady=5)

    tk.Label(encode_window, text="Enter Password:").pack(pady=5)
    password_entry = tk.Entry(encode_window, width=40, show="*")
    password_entry.pack(pady=5)

    def encode_and_save():
        image_path = image_path_entry.get()
        message = message_entry.get()
        password = password_entry.get()
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Images", "*.png")])

        if not image_path or not message or not password or not output_path:
            messagebox.showerror("Error", "All fields are required!")
            return

        encode_message(image_path, message, password, output_path)
        messagebox.showinfo("Success", "Message encoded and saved successfully!")

    tk.Button(encode_window, text="Encode and Save", command=encode_and_save).pack(pady=10)

def open_decode_window():
    decode_window = tk.Toplevel(root)
    decode_window.title("Decode Message")

    tk.Label(decode_window, text="Select Image File:").pack(pady=5)
    image_path_entry = tk.Entry(decode_window, width=40)
    image_path_entry.pack(pady=5)

    def select_image():
        image_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, image_path)

    tk.Button(decode_window, text="Browse", command=select_image).pack(pady=5)

    tk.Label(decode_window, text="Enter Password:").pack(pady=5)
    password_entry = tk.Entry(decode_window, width=40, show="*")
    password_entry.pack(pady=5)

    def decode_and_display():
        image_path = image_path_entry.get()
        password = password_entry.get()

        if not image_path or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        message = decode_message(image_path, password)
        if message:
            messagebox.showinfo("Hidden Message", message)
        else:
            messagebox.showerror("Error", "Failed to decode message or incorrect password.")

    tk.Button(decode_window, text="Decode", command=decode_and_display).pack(pady=10)

root = tk.Tk()
root.title("Steganography Tool")

tk.Button(root, text="Encode Message", command=open_encode_window).pack(pady=10)
tk.Button(root, text="Decode Message", command=open_decode_window).pack(pady=10)

root.mainloop()
