from controllers.paint_controller import PaintController
from models.drawing_canvas import DrawingCanvas
from views.main_window import MainWindow

def main():
    model = DrawingCanvas()
    view = MainWindow(None)  # Pass None as the controller for now
    controller = PaintController(model, view)
    view.controller = controller  # Set the controller in the view

    view.bind_mouse_events(controller.on_mouse_press, controller.on_mouse_drag, controller.on_mouse_release)
    view.bind_tool_buttons(controller.on_tool_select)
    view.bind_size_dropdown(controller.on_size_change)  # Bind the pen size dropdown

    view.mainloop()

if __name__ == "__main__":
    main()