import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Functions for encryption and decryption
def generate_key():
    # Generate a new encryption key
    return Fernet.generate_key()

def encrypt_message(message, key):
    # Encrypt the provided message using the given key
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    # Decrypt the provided encrypted message using the given key
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

# Functions for GUI
def encrypt_text():
    try:
        # Get the input text to encrypt
        message = entry_message.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Error", "Enter text to encrypt!")
            return
        
        # Encrypt the message and display the result
        encrypted_message = encrypt_message(message, current_key)
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, encrypted_message.decode())
    except Exception as e:
        # Show error if encryption fails
        messagebox.showerror("Error", f"Encryption failed: {e}")

def decrypt_text():
    try:
        # Get the input text to decrypt
        encrypted_message = entry_message.get("1.0", tk.END).strip()
        if not encrypted_message:
            messagebox.showerror("Error", "Enter encrypted text!")
            return
        
        # Decrypt the message and display the result
        decrypted_message = decrypt_message(encrypted_message.encode(), current_key)
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, decrypted_message)
    except Exception as e:
        # Show error if decryption fails
        messagebox.showerror("Error", f"Decryption failed: {e}")

def save_key():
    try:
        # Save the current key to a file
        with open("key.key", "wb") as file:
            file.write(current_key)
        messagebox.showinfo("Success", "Key saved to 'key.key'.")
    except Exception as e:
        # Show error if saving the key fails
        messagebox.showerror("Error", f"Failed to save key: {e}")

def load_key():
    try:
        # Load the key from a file
        global current_key
        with open("key.key", "rb") as file:
            current_key = file.read()
        messagebox.showinfo("Success", "Key loaded successfully.")
    except FileNotFoundError:
        # Handle case where key file does not exist
        messagebox.showerror("Error", "Key file not found. Generate a new key first!")
    except Exception as e:
        # Show error if loading the key fails
        messagebox.showerror("Error", f"Failed to load key: {e}")

# Initialize GUI
root = tk.Tk()
root.title("Text Encryptor and Decryptor")

# Generate the initial encryption key
current_key = generate_key()

# GUI Layout
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Input text area
tk.Label(frame, text="Enter text or encrypted text:").grid(row=0, column=0, padx=5, pady=5)
entry_message = tk.Text(frame, height=5, width=50)
entry_message.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Output text area
tk.Label(frame, text="Result:").grid(row=2, column=0, padx=5, pady=5)
entry_result = tk.Text(frame, height=5, width=50)
entry_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Buttons for encryption, decryption, saving and loading keys
tk.Button(frame, text="Encrypt", command=encrypt_text, bg="lightblue").grid(row=4, column=0, padx=5, pady=10, sticky="ew")
tk.Button(frame, text="Decrypt", command=decrypt_text, bg="lightgreen").grid(row=4, column=1, padx=5, pady=10, sticky="ew")

tk.Button(frame, text="Save Key", command=save_key).grid(row=5, column=0, padx=5, pady=10, sticky="ew")
tk.Button(frame, text="Load Key", command=load_key).grid(row=5, column=1, padx=5, pady=10, sticky="ew")

# Start the GUI application
root.mainloop()
