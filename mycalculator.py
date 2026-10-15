import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator App")
root.geometry("300x400")

# Entry widget to act as the calculator screen
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10, ipady=10)

# Function to update the screen when buttons are clicked
def click(val):
    display.insert(tk.END, val)

# Function to clear the screen
def clear():
    display.delete(0, tk.END)

# Function to calculate the final result
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Frame for buttons layout
btn_frame = tk.Frame(root)
btn_frame.pack()

# Define button labels
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

# Create and place buttons in a grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(btn_frame, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    elif text == 'C':
        btn = tk.Button(btn_frame, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    else:
        btn = tk.Button(btn_frame, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()