import tkinter as tk
from tkinter import Entry, Button, Label, messagebox
import numpy as np

def create_equation_inputs():
    global n, equation_entries
    n = int(entry_n.get())

    if n <= 0:
        messagebox.showerror("Lỗi", "Số ẩn phải lớn hơn 0")
        return

    if equation_entries:
        for row in equation_entries:
            for entry in row:
                entry.destroy()

    equation_entries = []
    for i in range(n):
        row_entries = []
        for j in range(n + 1):
            entry = Entry(root)
            entry.grid(row=i + 2, column=j)
            row_entries.append(entry)
        equation_entries.append(row_entries)

def solve_equations():
    global equation_entries
    coefficients = []
    for row in equation_entries:
        row_coeffs = []
        for entry in row:
            input_value = entry.get()
            if not input_value:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ các giá trị")
                return
            row_coeffs.append(float(input_value))
        coefficients.append(row_coeffs)

    A = np.array([row[:-1] for row in coefficients])
    b = np.array([row[-1] for row in coefficients])

    rank_A = np.linalg.matrix_rank(A)
    rank_Ab = np.linalg.matrix_rank(np.column_stack((A, b)))

    if rank_A < n:
        result_label.config(text="phương trình có vô nghiệm")
        return
    elif rank_A < n + 1:
        result_label.config(text="phương trình có vô số nghiệm")
        return
    elif rank_A == rank_Ab and rank_A == n:
        try:
            x = np.linalg.solve(A, b)
            result_label.config(text=f"Solution: {', '.join([f'x{i + 1} = {x[i]}' for i in range(n)])}")
        except np.linalg.LinAlgError:
            result_label.config(text="phương trình vô nghiệm")
            return
    else:
        result_label.config(text="phương trình có vô số nghiệm")

def clear_inputs():
    entry_n.delete(0, tk.END)
    result_label.config(text="")

    if equation_entries:
        for row in equation_entries:
            for entry in row:
                entry.destroy()
    equation_entries.clear()

root = tk.Tk()
root.title("Giải hệ phương trình")

lbl_n = Label(root, text="Nhập số ẩn (n):")
lbl_n.grid(row=0, column=0)
entry_n = Entry(root)
entry_n.grid(row=0, column=1)

create_button = Button(root, text="Tạo", command=create_equation_inputs)
create_button.grid(row=0, column=2)
solve_button = Button(root, text="Giải", command=solve_equations)
solve_button.grid(row=0, column=3)

clear_button = Button(root, text="Xóa", command=clear_inputs)
clear_button.grid(row=0, column=4)

result_label = Label(root, text="")
result_label.grid(row=1, columnspan=5)

equation_entries = []

root.mainloop()
