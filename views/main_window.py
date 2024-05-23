import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab

class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("MS Paint Clone")
        self.controller = controller

        self.menu_ribbon = tk.Frame(self)
        self.menu_ribbon.pack(side=tk.TOP, fill=tk.X)

        self.file_menu = tk.Menubutton(self.menu_ribbon, text="File")
        self.file_menu.pack(side=tk.LEFT, padx=5, pady=5)

        self.file_dropdown = tk.Menu(self.file_menu, tearoff=0)
        self.file_dropdown.add_command(label="New Canvas", command=self.new_file)
        self.file_dropdown.add_separator()
        self.file_dropdown.add_command(label="Save", command=self.save_file)
        self.file_dropdown.add_command(label="Save As", command=self.save_file_as)
        self.file_dropdown.add_separator()
        self.file_dropdown.add_command(label="Exit", command=self.quit)

        self.file_menu.config(menu=self.file_dropdown)

        self.toolbar = tk.Frame(self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.tool_frame = tk.Frame(self.toolbar)
        self.tool_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.pen_icon = self.load_icon("pen.png")
        self.pen_button = tk.Button(self.tool_frame, image=self.pen_icon, command=lambda: self.controller.on_tool_select("pen"))
        self.pen_button.pack(side=tk.TOP, padx=5, pady=5)

        self.eraser_icon = self.load_icon("eraser.png")
        self.eraser_button = tk.Button(self.tool_frame, image=self.eraser_icon, command=lambda: self.controller.on_tool_select("eraser"))
        self.eraser_button.pack(side=tk.TOP, padx=5, pady=5)

        self.size_var = tk.StringVar(value="2")
        self.size_dropdown = tk.OptionMenu(self.tool_frame, self.size_var, "2", "4", "6", "8", "10")
        self.size_dropdown.pack(side=tk.TOP, padx=5, pady=5)

        self.color_frame = tk.Frame(self.toolbar)
        self.color_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.colors = [
            "black", "white", "red", "green", "blue",
            "yellow", "orange", "purple", "pink", "brown",
            "gray", "cyan", "magenta", "gold", "silver"
        ]

        for i, color in enumerate(self.colors):
            color_button = tk.Button(self.color_frame, bg=color, width=2, height=1,
                                     command=lambda c=color: self.controller.on_color_select(c))
            color_button.grid(row=i // 5, column=i % 5, padx=2, pady=2)

        self.drawing_canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.drawing_canvas.pack(fill=tk.BOTH, expand=True)

        self.current_file = None


    def load_icon(self, filename):
        icon = Image.open(filename)
        icon = icon.resize((24, 24), Image.LANCZOS)
        return ImageTk.PhotoImage(icon)

    def show_description(self, text):
        self.description_label.config(text=text)
        self.description_label.pack(side=tk.LEFT)

    def hide_description(self, event):
        self.description_label.pack_forget()

    def bind_mouse_events(self, on_mouse_press, on_mouse_drag, on_mouse_release):
        self.drawing_canvas.bind("<Button-1>", on_mouse_press)
        self.drawing_canvas.bind("<B1-Motion>", on_mouse_drag)
        self.drawing_canvas.bind("<ButtonRelease-1>", on_mouse_release)

    def bind_tool_buttons(self, on_tool_select):
        self.pen_button.config(command=lambda: on_tool_select("pen"))
        self.eraser_button.config(command=lambda: on_tool_select("eraser"))

    def bind_size_dropdown(self, on_size_change):
        self.size_var.trace("w", lambda *args: on_size_change(self.size_var.get()))


    def draw_line(self, start, end, color, width):
        self.drawing_canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=width)

    def erase(self, start, end, width):
        self.drawing_canvas.create_line(start[0], start[1], end[0], end[1], fill="white", width=width)

    def save_file(self):
        if self.current_file:
            self.save_canvas_as_png(self.current_file)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if file_path:
            self.current_file = file_path
            self.save_canvas_as_png(file_path)

    def save_canvas_as_png(self, file_path):
        # Get the coordinates of the drawing canvas
        x = self.drawing_canvas.winfo_rootx()
        y = self.drawing_canvas.winfo_rooty()
        x1 = x + self.drawing_canvas.winfo_width()
        y1 = y + self.drawing_canvas.winfo_height()

        # Calculate the heights of the menu ribbon and toolbar
        menu_height = self.menu_ribbon.winfo_height()
        toolbar_height = self.toolbar.winfo_height()

        # Adjust the y-coordinate to account for the menu ribbon and toolbar heights
        y += menu_height + toolbar_height

        # Capture the drawing canvas area
        image = ImageGrab.grab().crop((x, y, x1, y1))
        image.save(file_path)

    def new_file(self):
        if messagebox.askyesno("New Canvas", "Are you sure you want to start a new canvas? All unsaved changes will be lost."):
            self.drawing_canvas.delete("all")
            self.current_file = None