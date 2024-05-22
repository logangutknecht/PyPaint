from controllers.paint_controller import PaintController
from models.drawing_canvas import DrawingCanvas
from views.main_window import MainWindow

def main():
    model = DrawingCanvas()
    view = MainWindow(None)  # Pass None as the controller for now
    controller = PaintController(model, view)
    view.controller = controller  # Set the controller in the view

    view.mainloop()

if __name__ == "__main__":
    main()