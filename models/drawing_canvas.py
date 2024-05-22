class DrawingCanvas:
    def __init__(self):
        self.shapes = []

    def start_drawing(self, x, y, color, width):
        self.shapes.append({"type": "line", "points": [(x, y)], "color": color, "width": width})

    def draw_line(self, x, y):
        self.shapes[-1]["points"].append((x, y))

    def start_erasing(self, x, y, width):
        self.shapes.append({"type": "erasure", "points": [(x, y)], "width": width})

    def erase(self, x, y, width):
        self.shapes[-1]["points"].append((x, y))
        self.shapes[-1]["width"] = width

    def get_last_point(self):
        return self.shapes[-1]["points"][-2]

    def get_last_width(self):
        return self.shapes[-1]["width"]