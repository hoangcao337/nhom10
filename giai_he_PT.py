import tkinter as tk
from tkinter import Entry, Button, Label, messagebox
import numpy as np

def create_equation_inputs():
    global n
    try:
        n = int(entry_n.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Số ẩn phải là một số nguyên")
        return

    if n <= 0:
        messagebox.showerror("Lỗi", "Số ẩn phải lớn hơn 0")
        return

    for i in range(n):
        for j in range(n + 1):
            entry = Entry(root, bg='light blue')
            entry.grid(row=i + 2, column=j)

def solve_equations():
    global n
    coefficients = []
    for i in range(n):
        row_coeffs = []
        for j in range(n + 1):
            input_value = root.grid_slaves(i + 2, j)[0].get()
            if not input_value:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ các giá trị")
                return
            row_coeffs.append(float(input_value))
        coefficients.append(row_coeffs)

    result = solve(coefficients)
    messagebox.showinfo("Kết quả", result)

def solve(coefficients):
    n = len(coefficients)
    A = np.array([row[:-1] for row in coefficients])
    b = np.array([row[-1] for row in coefficients])

    try:
        x = np.linalg.solve(A, b)
        return f"Nghiệm: {', '.join([f'x{i + 1} = {x[i]}' for i in range(n)])}"
    except np.linalg.LinAlgError:
        return "Hệ phương trình vô nghiệm hoặc có vô số nghiệm"

def clear_inputs():
    global n
    entry_n.delete(0, tk.END)

    for i in range(n):
        for j in range(n + 1):
            root.grid_slaves(i + 2, j)[0].destroy()

root = tk.Tk()
root.title("Giải hệ phương trình")
root.configure(bg='light green')

lbl_n = Label(root, text="Nhập số ẩn (n):", bg='light green')
lbl_n.grid(row=0, column=0)
entry_n = Entry(root, bg='light blue')
entry_n.grid(row=0, column=1)

create_button = Button(root, text="Tạo", command=create_equation_inputs, bg='light yellow')
create_button.grid(row=0, column=2)
solve_button = Button(root, text="Giải", command=solve_equations, bg='light yellow')
solve_button.grid(row=0, column=3)

clear_button = Button(root, text="Xóa", command=clear_inputs, bg='light yellow')
clear_button.grid(row=0, column=4)

exit_button = Button(root, text="Thoát", command=root.destroy, bg='light yellow')
exit_button.grid(row=0, column=5)

root.mainloop()
