import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from population_data import PopulationData  # импорт класса Екатерины

class PopulationApp(tk.Tk):
    """Основное приложение с графическим интерфейсом"""

    def __init__(self):
        super().__init__()
        self.title("Статистика населения России")
        self.geometry("900x600")
        self.data = None
