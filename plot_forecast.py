import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui_app import PopulationApp  # импорт класса интерфейса

class PopulationAppWithPlot(PopulationApp):
    """Добавление графиков и прогноза к основному интерфейсу"""
        def plot_data(self):
        if not self.data:
            messagebox.showwarning("Внимание", "Сначала загрузите файл с данными!")
            return

    pass
