import tkinter as tk
from tkinter import Entry, Button, Label
import numpy as np


def create_equation_inputs():
    global n, equation_entries
    n = int(entry_n.get())

    # Xóa các widget hệ số cũ nếu có
    if equation_entries:
        for row in equation_entries:
            for entry in row:
                entry.destroy()

    # Tạo bảng nhập hệ số
    equation_entries = []
    for i in range(n):
        row_entries = []
        for j in range(n + 1):
            entry = Entry(root)
            entry.grid(row=i + 2, column=j)
            row_entries.append(entry)
        equation_entries.append(row_entries)


def solve_equations():
    coefficients = []
    for row in equation_entries:
        row_coeffs = []
        for entry in row:
            row_coeffs.append(float(entry.get()))
        coefficients.append(row_coeffs)

    # Chuyển danh sách hệ số thành mảng NumPy
    A = np.array([row[:-1] for row in coefficients])
    b = np.array([row[-1] for row in coefficients])

    # Giải hệ phương trình
    try:
        x = np.linalg.solve(A, b)
        result_label.config(text=f"Kết quả: x = {x}")
    except np.linalg.LinAlgError:
        result_label.config(text="Hệ phương trình không có nghiệm")


def clear_inputs():
    entry_n.delete(0, tk.END)
    result_label.config(text="")

    # Xóa các widget hệ số cũ nếu có
    if equation_entries:
        for row in equation_entries:
            for entry in row:
                entry.destroy()
    equation_entries.clear()


# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Giải hệ phương trình")

# Widget và nút nhập n
lbl_n = Label(root, text="Nhập số ẩn (n):")
lbl_n.grid(row=0, column=0)
entry_n = Entry(root)
entry_n.grid(row=0, column=1)

# Nút tạo và nút giải
create_button = Button(root, text="Tạo", command=create_equation_inputs)
create_button.grid(row=0, column=2)
solve_button = Button(root, text="Giải", command=solve_equations)
solve_button.grid(row=0, column=3)

# Nút xóa
clear_button = Button(root, text="Xóa", command=clear_inputs)
clear_button.grid(row=0, column=4)

# Label hiển thị kết quả
result_label = Label(root, text="")
result_label.grid(row=1, columnspan=5)

equation_entries = []

root.mainloop()
