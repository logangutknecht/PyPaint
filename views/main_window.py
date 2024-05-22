import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("MS Paint Clone")
        self.controller = controller

        self.drawing_canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.drawing_canvas.pack()

        self.pen_button = tk.Button(self, text="Pen", command=lambda: self.controller.on_tool_select("pen"))
        self.pen_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(self, text="Eraser", command=lambda: self.controller.on_tool_select("eraser"))
        self.eraser_button.pack(side=tk.LEFT)

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