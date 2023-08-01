import tkinter as tk
from tkinter import filedialog


def choose_excel_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        parent=root, filetypes=[("Excel Files", "*.xlsx")]
    )
    return file_path
