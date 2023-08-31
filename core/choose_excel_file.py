from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox as mb


def choose_excel_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        parent=root, filetypes=[("Excel Files", "*.xlsx")], title="Выберите файл: ZAKAZ.xlsx"
    )
    return file_path


def show_info():
    msg = "Импорт завершен"
    mb.showinfo("Информация", msg)

