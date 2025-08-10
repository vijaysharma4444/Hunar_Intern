import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def process_cipher():
    mode = mode_var.get()
    message = message_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "🔢 Shift must be a number.")
        return

    if mode == "Encrypt":
        result = caesar_encrypt(message, shift)
    else:
        result = caesar_decrypt(message, shift)

    result_var.set(result)

def clear_fields():
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    result_var.set("")

# GUI Setup
root = tk.Tk()
root.title("🔐 Caesar Cipher Tool")
root.geometry("450x350")
root.configure(bg="#f0f4f7")
root.resizable(False, False)

# Title
tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

# Frame for Inputs
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=5)

# Mode Selection
tk.Label(frame, text="🔄 Mode:", bg="#f0f4f7", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
mode_var = tk.StringVar(value="Encrypt")
tk.OptionMenu(frame, mode_var, "Encrypt", "Decrypt").grid(row=0, column=1, padx=5, pady=5)

# Message Entry
tk.Label(frame, text="✉️ Message:", bg="#f0f4f7", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
message_entry = tk.Entry(frame, width=30, font=("Arial", 11))
message_entry.grid(row=1, column=1, padx=5, pady=5)

# Shift Entry
tk.Label(frame, text="🔢 Shift:", bg="#f0f4f7", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
shift_entry = tk.Entry(frame, width=10, font=("Arial", 11))
shift_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

tk.Button(button_frame, text="🔐 Run Cipher", command=process_cipher, bg="#4CAF50", fg="white", font=("Arial", 11), width=15).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="🧹 Clear", command=clear_fields, bg="#f44336", fg="white", font=("Arial", 11), width=10).grid(row=0, column=1)

# Result Display
tk.Label(root, text="📄 Result:", bg="#f0f4f7", font=("Arial", 12)).pack()
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=40, font=("Arial", 12), state="readonly", justify="center").pack(pady=5)

# Run the GUI
root.mainloop()