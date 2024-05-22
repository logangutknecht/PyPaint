class PaintController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_tool = "pen"
        self.current_color = "black"
        self.is_drawing = False

        self.view.bind_mouse_events(self.on_mouse_press, self.on_mouse_drag, self.on_mouse_release)
        self.view.bind_tool_buttons(self.on_tool_select)

    def on_mouse_press(self, event):
        if self.current_tool == "pen":
            self.is_drawing = True
            self.model.start_drawing(event.x, event.y, self.current_color)
        elif self.current_tool == "eraser":
            self.is_drawing = True
            self.model.start_erasing(event.x, event.y)

    def on_mouse_drag(self, event):
        if self.is_drawing:
            if self.current_tool == "pen":
                self.model.draw_line(event.x, event.y)
                self.view.draw_line(self.model.get_last_point(), (event.x, event.y), self.current_color)
            elif self.current_tool == "eraser":
                self.model.erase(event.x, event.y)
                self.view.erase(self.model.get_last_point(), (event.x, event.y))

    def on_mouse_release(self, event):
        self.is_drawing = False

    def on_tool_select(self, tool):
        self.current_tool = tool