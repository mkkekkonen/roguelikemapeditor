import tkinter as tk

from mapeditor.map_window import display_map_window


def ask_dimensions():
    def submit():
        canvas_width = int(width_entry.get())
        canvas_height = int(height_entry.get())
        dimension_window.destroy()
        display_map_window(canvas_width, canvas_height)

    dimension_window = tk.Tk()
    dimension_window.title("Enter Canvas Dimensions")

    tk.Label(dimension_window, text="Width:").pack()
    width_entry = tk.Entry(dimension_window)
    width_entry.pack()

    tk.Label(dimension_window, text="Height:").pack()
    height_entry = tk.Entry(dimension_window)
    height_entry.pack()

    submit_button = tk.Button(dimension_window, text="Submit", command=submit)
    submit_button.pack()

    dimension_window.mainloop()
