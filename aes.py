import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt data
def encrypt_data(data, key, mode):
    if mode == "CBC":
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size, style="pkcs7"))
        return iv.hex() + ":" + ct_bytes.hex().upper()
    else:  # ECB
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size, style="pkcs7"))
        return ct_bytes.hex().upper()

# Function to decrypt data
def decrypt_data(encrypted_data, key, mode):
    try:
        if mode == "CBC":
            iv_hex, ct_hex = encrypted_data.split(":")
            iv = bytes.fromhex(iv_hex)
            ct_bytes = bytes.fromhex(ct_hex)
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        else:  # ECB
            ct_bytes = bytes.fromhex(encrypted_data)
            cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        
        pt = unpad(cipher.decrypt(ct_bytes), AES.block_size, style="pkcs7")
        return pt.decode('utf-8')
    except (ValueError, KeyError):
        return "Decryption failed. Invalid data, key, or padding."

# Input validation function
def validate_key(key):
    if len(key) != 16:
        messagebox.showerror("Invalid Key", "Key must be 16 characters long.")
        return False
    return True

# Function to handle Encryption button
def on_encrypt():
    text = entry_text.get("1.0", tk.END).strip()
    key = entry_key.get()
    mode = mode_var.get()

    if not validate_key(key):
        return

    if not text:
        messagebox.showerror("Invalid Input", "Text cannot be empty.")
        return

    encrypted = encrypt_data(text, key, mode)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Encrypted Text:\n{encrypted}")
    result_text.config(state=tk.DISABLED)

# Function to handle Decryption button
def on_decrypt():
    encrypted_text = entry_text.get("1.0", tk.END).strip()
    key = entry_key.get()
    mode = mode_var.get()

    if not validate_key(key):
        return

    if not encrypted_text:
        messagebox.showerror("Invalid Input", "Encrypted text cannot be empty.")
        return

    decrypted = decrypt_data(encrypted_text, key, mode)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Decrypted Text:\n{decrypted}")
    result_text.config(state=tk.DISABLED)

# Main Application Window
root = tk.Tk()
root.title("AES Encryption/Decryption Tool")
root.geometry("600x500")
root.resizable(False, False)

# Frame for Key Input
key_frame = ttk.Frame(root, padding=10)
key_frame.pack(fill=tk.X)

key_label = ttk.Label(key_frame, text="Enter 16-character Key:")
key_label.pack(side=tk.LEFT, padx=(0, 5))

entry_key = ttk.Entry(key_frame, show="*", width=40)
entry_key.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Frame for Mode Selection
mode_frame = ttk.Frame(root, padding=10)
mode_frame.pack(fill=tk.X)

mode_label = ttk.Label(mode_frame, text="Select AES Mode:")
mode_label.pack(side=tk.LEFT, padx=(0, 5))

mode_var = tk.StringVar(value="CBC")
cbc_radio = ttk.Radiobutton(mode_frame, text="CBC", variable=mode_var, value="CBC")
cbc_radio.pack(side=tk.LEFT, padx=5)

ecb_radio = ttk.Radiobutton(mode_frame, text="ECB", variable=mode_var, value="ECB")
ecb_radio.pack(side=tk.LEFT, padx=5)

# Frame for Input Text
input_frame = ttk.LabelFrame(root, text="Input Text", padding=10)
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

entry_text = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, height=10)
entry_text.pack(fill=tk.BOTH, expand=True)

# Frame for Buttons
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(fill=tk.X)

encrypt_button = ttk.Button(button_frame, text="Encrypt", command=on_encrypt)
encrypt_button.pack(side=tk.LEFT, padx=(0, 5))

decrypt_button = ttk.Button(button_frame, text="Decrypt", command=on_decrypt)
decrypt_button.pack(side=tk.LEFT, padx=(5, 0))

# Frame for Output Text
output_frame = ttk.LabelFrame(root, text="Output", padding=10)
output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

result_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=10, state=tk.DISABLED)
result_text.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter main loop
root.mainloop()