import tkinter as tk
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("PyPaint")
        self.controller = controller

        self.toolbar = tk.Frame(self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.pen_icon = self.load_icon("pen.png")
        self.pen_button = tk.Button(self.toolbar, image=self.pen_icon, command=lambda: self.controller.on_tool_select("pen"))
        self.pen_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.pen_button.bind("<Enter>", lambda event: self.show_description("Pen"))
        self.pen_button.bind("<Leave>", self.hide_description)

        self.eraser_icon = self.load_icon("eraser.png")
        self.eraser_button = tk.Button(self.toolbar, image=self.eraser_icon, command=lambda: self.controller.on_tool_select("eraser"))
        self.eraser_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.eraser_button.bind("<Enter>", lambda event: self.show_description("Eraser"))
        self.eraser_button.bind("<Leave>", self.hide_description)

        self.description_label = tk.Label(self.toolbar, text="", fg="black", bg="white", padx=5, pady=2)

        self.drawing_canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.drawing_canvas.pack(fill=tk.BOTH, expand=True)

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

    def draw_line(self, start, end, color):
        self.drawing_canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=2)

    def erase(self, start, end):
        self.drawing_canvas.create_line(start[0], start[1], end[0], end[1], fill="white", width=10)