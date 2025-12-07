import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi

# Initialize memory variable
memory = 0

# Function to handle button clicks
def button_click(value):
    global memory
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "M+":
        try:
            memory = eval(entry.get())
            entry.delete(0, tk.END)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "MR":
        entry.insert(tk.END, str(memory))
    elif value == "MC":
        memory = 0
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value in ["sin", "cos", "tan", "log", "sqrt", "pi"]:
        try:
            if value == "sin":
                result = sin(eval(entry.get()))
            elif value == "cos":
                result = cos(eval(entry.get()))
            elif value == "tan":
                result = tan(eval(entry.get()))
            elif value == "log":
                result = log(eval(entry.get()))
            elif value == "sqrt":
                result = sqrt(eval(entry.get()))
            elif value == "pi":
                entry.insert(tk.END, str(pi))
                return
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

# Create the main window
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("400x600")
window.resizable(True, True)

# Create an entry widget
entry = tk.Entry(window, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define button labels
buttons = [
    "C", "M+", "MR", "MC", "/",
    "7", "8", "9", "*", "sin",
    "4", "5", "6", "-", "cos",
    "1", "2", "3", "+", "tan",
    "0", ".", "=", "sqrt", "log",
    "(", ")", "pi", "^", "%"
]

# Create buttons and add them to the grid
row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(
        window,
        text=button,
        font=("Arial", 15),
        bg="lightgray",
        fg="black",
        width=6,
        height=2,
        command=lambda b=button: button_click(b)
    )
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Run the application
window.mainloop()
