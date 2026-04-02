import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# COPY CODE THUẬT TOÁN ECC TỪ BÀI LAB CŨ CỦA BẠN VÀO ĐÂY
# ---------------------------------------------------------
def encryptECC(text):
    # Dummy logic - Thay bằng hàm mã hóa thực tế
    return f"Đã mã hóa ECC: {text}"

def decryptECC(cipher):
    # Dummy logic - Thay bằng hàm giải mã thực tế
    return f"Đã giải mã ECC: {cipher}"

def execute_ecc():
    msg = entry_text.get()
    if var_mode.get() == 1:
        res = encryptECC(msg)
    else:
        res = decryptECC(msg)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, res)

# Tạo UI
root = tk.Tk()
root.title("ECC Cipher UI")
root.geometry("400x250")

tk.Label(root, text="Nhập bản rõ / Bản mã:").pack(pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.pack()

var_mode = tk.IntVar(value=1)
tk.Radiobutton(root, text="Mã hóa ECC", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="Giải mã ECC", variable=var_mode, value=2).pack()

tk.Button(root, text="Thực hiện", command=execute_ecc, bg="lightgreen").pack(pady=10)

text_result = tk.Text(root, height=4, width=50)
text_result.pack()

root.mainloop()