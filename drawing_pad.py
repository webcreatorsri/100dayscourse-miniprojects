import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw

# Main Window
root = tk.Tk()
root.title("Drawing Pad App")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Global Variables
current_color = "black"
current_thickness = 2
drawing_mode = "draw"  # Modes: 'draw', 'erase'
undo_stack = []
redo_stack = []

# Create Canvas
canvas = tk.Canvas(root, width=500, height=400, bg="white", relief="ridge", bd=2)
canvas.pack(pady=20)

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    if drawing_mode == "erase":
        color = "white"
    else:
        color = current_color
    
    line = canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=current_thickness, capstyle=tk.ROUND, smooth=True)
    undo_stack.append(line)
    last_x, last_y = event.x, event.y

def clear_canvas():
    canvas.delete("all")
    undo_stack.clear()
    redo_stack.clear()

def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

def toggle_eraser():
    global drawing_mode
    drawing_mode = "erase" if drawing_mode == "draw" else "draw"
    eraser_button.config(text="Eraser" if drawing_mode == "erase" else "Brush")

def save_canvas():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        for item in canvas.find_all():
            x1, y1, x2, y2 = canvas.coords(item)
            color = canvas.itemcget(item, "fill")
            draw.line([(x1, y1), (x2, y2)], fill=color, width=current_thickness)
        image.save(file_path)

def undo():
    if undo_stack:
        last_action = undo_stack.pop()
        redo_stack.append(last_action)
        canvas.delete(last_action)

def redo():
    if redo_stack:
        last_action = redo_stack.pop()
        canvas.itemconfig(last_action, state="normal")
        undo_stack.append(last_action)

# Bind Drawing
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Control Panel
control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=10)

color_btn = tk.Button(control_frame, text="Choose Color", command=change_color, bg="white", fg="black", font=("Arial", 10))
color_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(control_frame, text="Clear Canvas", command=clear_canvas, bg="white", fg="black", font=("Arial", 10))
clear_btn.grid(row=0, column=1, padx=10)

eraser_button = tk.Button(control_frame, text="Brush", command=toggle_eraser, bg="white", fg="black", font=("Arial", 10))
eraser_button.grid(row=0, column=2, padx=10)

thickness_label = tk.Label(control_frame, text="Thickness:", bg="#f0f0f0", font=("Arial", 10))
thickness_label.grid(row=0, column=3, padx=10)

thickness_slider = tk.Scale(control_frame, from_=1, to=10, orient="horizontal", command=change_thickness, bg="#f0f0f0")
thickness_slider.set(2)
thickness_slider.grid(row=0, column=4, padx=10)

undo_btn = tk.Button(control_frame, text="Undo", command=undo, bg="white", fg="black", font=("Arial", 10))
undo_btn.grid(row=0, column=5, padx=10)

redo_btn = tk.Button(control_frame, text="Redo", command=redo, bg="white", fg="black", font=("Arial", 10))
redo_btn.grid(row=0, column=6, padx=10)

save_btn = tk.Button(control_frame, text="Save", command=save_canvas, bg="white", fg="black", font=("Arial", 10))
save_btn.grid(row=0, column=7, padx=10)

# Run Application
root.mainloop()