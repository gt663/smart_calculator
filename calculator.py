import tkinter as tk
import math
import threading

def button_click(event):
    # Function to handle button click events
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        # Start a new thread to perform the calculation
        t = threading.Thread(target=calculate_result, args=(current,))
        t.start()
    elif text == "C":
        # Clear the entry widget
        entry.delete(0, tk.END)
    elif text == "Del":
        # Delete the last character in the entry widget
        entry.delete(len(entry.get()) - 1)
    elif text == "sin":
        # Insert "math.sin(" or "math.sin(math.radians(" depending on the mode
        if mode.get() == "D":
            entry.insert(tk.END, "math.sin(math.radians(")
        else:
            entry.insert(tk.END, "math.sin(")
    elif text == "cos":
        # Insert "math.cos(" or "math.cos(math.radians(" depending on the mode
        if mode.get() == "D":
            entry.insert(tk.END, "math.cos(math.radians(")
        else:
            entry.insert(tk.END, "math.cos(")
    elif text == "tan":
        # Insert "math.tan(" or "math.tan(math.radians(" depending on the mode
        if mode.get() == "D":
            entry.insert(tk.END, "math.tan(math.radians(")
        else:
            entry.insert(tk.END, "math.tan(")
    elif text == "log":
        # Insert "math.log10(" for logarithm calculation
        entry.insert(tk.END, "math.log10(")
    elif text == "sqrt":
        # Insert "math.sqrt(" for square root calculation
        entry.insert(tk.END, "math.sqrt(")
    elif text == "Degrees":
        # Set the mode to "degrees"
        mode.set("D")
    elif text == "Radians":
        # Set the mode to "radians"
        mode.set("R")
    elif text == "π":
        # Insert "math.pi" for the constant π (pi)
        entry.insert(tk.END, "math.pi")
    else:
        # Insert the button text into the entry widget
        entry.insert(tk.END, text)

def calculate_result(expression):
    # Function to calculate the result
    try:
        if mode.get() == "D":
            # Evaluate the expression while converting degrees to radians if in degrees mode
            result = eval(expression.replace("math.degrees", ""))
        else:
            # Evaluate the expression as is if in radians mode
            result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        # Handle any errors that occur during evaluation
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def show_buttons(row, col):
    # Function to display the buttons on the calculator
    if row < num_rows:
        if col < len(buttons[row]):
            button_text = buttons[row][col]
            button_color = "yellow" if button_text in ["Del", "C", "Degrees", "Radians"] else "gray"
            # Create and configure the button
            button = tk.Button(root, text=button_text, font=("Arial", 12), width=5, bg=button_color)
            button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="wens")
            button.bind("<Button-1>", button_click)
            col += 1
        else:
            col = 0
            row += 1

        # Schedule the next button display
        root.after(100, show_buttons, row, col)

# Create the main window
root = tk.Tk()
root.geometry("450x450")  # Set the window size
root.title("Scientific Calculator")  # Set the window title
root.configure(bg="white")  # Set the background color to gray
root.resizable(width=True, height=True)  # Allow window resizing

# Variable to store the mode (degrees or radians)
mode = tk.StringVar()
mode.set("R")  # Set the initial mode to radians

# Create the entry widget
entry = tk.Entry(root, font=("Arial", 20), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="we")

# Create the mode label
mode_label = tk.Label(root, textvariable=mode, font=("Arial", 12, "bold"), fg="black")
mode_label.grid(row=0, column=5, padx=5, pady=10, sticky="w")

# Create the buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "cos", "+"],
    ["(", ")", "Del", "C"],
    ["log", "tan", "sin", "="],
    ["sqrt", "π", "Degrees", "Radians"]
]

num_rows = len(buttons)
num_cols = max(len(row) for row in buttons)

# Start showing buttons
show_buttons(0, 0)

# Configure column weights to make buttons stretch
for i in range(num_cols):
    root.columnconfigure(i, weight=1)

# Configure row weight to make buttons stretch in height
for i in range(num_rows + 1):
    root.rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
