import tkinter as tk
from tkinter import messagebox
import math

def encryptMessage(key, message):
    cipher = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key
    return "".join(cipher)

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [""] * numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return "".join(plaintext)

def execute():
    msg = entry_text.get()
    try:
        k = int(entry_key.get())
        if var_mode.get() == 1:
            res = encryptMessage(k, msg)
        else:
            res = decryptMessage(k, msg)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, res)
    except ValueError:
        messagebox.showerror("Lỗi", "Key phải là số nguyên!")

# Tạo UI
root = tk.Tk()
root.title("Transposition Cipher UI")
root.geometry("400x300")

tk.Label(root, text="Nhập chuỗi:").pack(pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.pack()

tk.Label(root, text="Nhập Key (Số nguyên):").pack(pady=5)
entry_key = tk.Entry(root, width=50)
entry_key.pack()

var_mode = tk.IntVar(value=1)
tk.Radiobutton(root, text="Mã hóa (Encrypt)", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="Giải mã (Decrypt)", variable=var_mode, value=2).pack()

tk.Button(root, text="Thực hiện", command=execute, bg="lightblue").pack(pady=10)

text_result = tk.Text(root, height=5, width=50)
text_result.pack()

root.mainloop()