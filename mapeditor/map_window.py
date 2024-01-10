import tkinter as tk
from tkinter import ttk


def display_map_window(canvas_width, canvas_height):
    window = tk.Tk()

    window.title("Map Editor")

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    left_frame = tk.Frame(window)
    right_frame = tk.Frame(window)

    left_frame.grid(row=0, column=0, sticky="nsew")
    right_frame.grid(row=0, column=1, sticky="nsew")

    canvas = tk.Canvas(left_frame, width=canvas_width, height=canvas_height)

    v_scrollbar = ttk.Scrollbar(
        left_frame, orient="vertical", command=canvas.yview)
    h_scrollbar = ttk.Scrollbar(
        left_frame, orient="horizontal", command=canvas.xview)

    canvas.grid(row=0, column=0, sticky="nsew")
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scrollbar.set,
                     xscrollcommand=h_scrollbar.set)

    left_frame.grid_rowconfigure(0, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    window.mainloop()
