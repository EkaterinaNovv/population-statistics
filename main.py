import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PopulationData:
    """Класс для хранения и обработки данных о населении"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
        self.data['Прирост, %'] = self.data['Население'].pct_change() * 100

    def max_growth(self):
        return self.data['Прирост, %'].max()

    def max_decline(self):
        return self.data['Прирост, %'].min()

    def moving_average_forecast(self, years=5, window=3):
        forecast = []
        last_window = self.data['Население'].tail(window).tolist()
        for _ in range(years):
            avg = sum(last_window[-window:]) / window
            forecast.append(avg)
            last_window.append(avg)
        return forecast


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

    def plot_data(self):
        if not self.data:
            messagebox.showwarning("Внимание", "Сначала загрузите файл с данными!")
            return

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(self.data.data['Год'], self.data.data['Население'], marker='o', label='Фактическое население')

        # Прогноз
        forecast_years = 5
        forecast = self.data.moving_average_forecast(years=forecast_years)
        last_year = self.data.data['Год'].iloc[-1]
        forecast_years_range = [last_year + i + 1 for i in range(forecast_years)]
        ax.plot(forecast_years_range, forecast, marker='o', linestyle='--', color='red', label='Прогноз')

        ax.set_title("Население России")
        ax.set_xlabel("Год")
        ax.set_ylabel("Население")
        ax.legend()

        # Показать на Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Вывод макс прироста и убыли
        growth = self.data.max_growth()
        decline = self.data.max_decline()
        messagebox.showinfo("Статистика", f"Максимальный прирост: {growth:.2f}%\nМаксимальная убыль: {decline:.2f}%")



if __name__ == "__main__":
    app = PopulationApp()
    app.mainloop()
