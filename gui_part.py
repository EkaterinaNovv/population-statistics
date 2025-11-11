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
        # Кнопка загрузки файла
        self.load_button = tk.Button(self, text="Открыть файл с данными", command=self.load_file)
        self.load_button.pack(pady=10)

        # Кнопка для построения графика
        self.plot_button = tk.Button(self, text="Построить график", command=self.plot_data)
        self.plot_button.pack(pady=10)
