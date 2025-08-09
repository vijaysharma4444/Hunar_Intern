import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    return score

def update_strength_bar(event=None):
    password = entry.get()
    score = check_password_strength(password)
    strength_bar["value"] = score * 20

    if score <= 2:
        result_label.config(text="Weak", foreground="red")
        style.configure("red.Horizontal.TProgressbar", thickness=10, background="red", troughcolor="#f0f0f0", bordercolor="#f0f0f0")
        strength_bar.config(style="red.Horizontal.TProgressbar")
    elif score == 3 or score == 4:
        result_label.config(text="Good", foreground="orange")
        style.configure("orange.Horizontal.TProgressbar", thickness=10, background="orange", troughcolor="#f0f0f0", bordercolor="#f0f0f0")
        strength_bar.config(style="orange.Horizontal.TProgressbar")
    else:
        result_label.config(text="Strong", foreground="green")
        style.configure("green.Horizontal.TProgressbar", thickness=10, background="green", troughcolor="#f0f0f0", bordercolor="#f0f0f0")
        strength_bar.config(style="green.Horizontal.TProgressbar")

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        eye_button.config(image=eye_closed_icon)
    else:
        entry.config(show='')
        eye_button.config(image=eye_icon)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x280")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")

main_frame = ttk.Frame(root, padding="20 10 20 10")
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Enter Password:", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="w", pady=5)

entry_frame = ttk.Frame(main_frame)
entry_frame.grid(row=1, column=0, sticky="w")

entry = ttk.Entry(entry_frame, show="*", font=("Segoe UI", 11), width=30)
entry.pack(side="left", ipady=3)
entry.bind("<KeyRelease>", update_strength_bar)

eye_img = Image.open("eye.png").resize((18, 18), Image.LANCZOS)
eye_closed_img = Image.open("eye_closed.png").resize((18, 18), Image.LANCZOS)

eye_icon = ImageTk.PhotoImage(eye_img)
eye_closed_icon = ImageTk.PhotoImage(eye_closed_img)

eye_button = tk.Button(entry_frame, image=eye_closed_icon, command=toggle_password, relief="flat", bg="white", bd=0)
eye_button.pack(side="left", padx=3)

# Compact, smooth bar
strength_bar = ttk.Progressbar(main_frame, length=250, mode='determinate')
strength_bar.grid(row=2, column=0, pady=10)

result_label = ttk.Label(main_frame, text="", font=("Segoe UI", 12, "bold"))
result_label.grid(row=3, column=0, pady=5)

root.mainloop()