class DrawingCanvas:
    def __init__(self):
        self.shapes = []

    def start_drawing(self, x, y, color):
        self.shapes.append({"type": "line", "points": [(x, y)], "color": color})

    def draw_line(self, x, y):
        self.shapes[-1]["points"].append((x, y))

    def start_erasing(self, x, y):
        self.shapes.append({"type": "erasure", "points": [(x, y)]})

    def erase(self, x, y):
        self.shapes[-1]["points"].append((x, y))

    def get_last_point(self):
        return self.shapes[-1]["points"][-2]