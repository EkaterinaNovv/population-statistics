import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from population_data import PopulationData 

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

        # Таблица для отображения данных
        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill='both')

        # Кнопка для построения графика
        self.plot_button = tk.Button(self, text="Построить график", command=self.plot_data)
        self.plot_button.pack(pady=10)

    def load_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            try:
                self.data = PopulationData(filepath)
                self.show_table()
                messagebox.showinfo("Успех", f"Файл {filepath} загружен")
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    def show_table(self):
        # Очистка старой таблицы
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Настройка колонок
        self.tree["columns"] = list(self.data.data.columns)
        self.tree["show"] = "headings"
        for col in self.data.data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Добавление данных
        for _, row in self.data.data.iterrows():
            self.tree.insert("", "end", values=list(row))
