import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui_app import PopulationApp  # импорт класса интерфейса

class PopulationAppWithPlot(PopulationApp):
    """Добавление графиков и прогноза к основному интерфейсу"""
        def plot_data(self):
        if not self.data:
            messagebox.showwarning("Внимание", "Сначала загрузите файл с данными!")
            return

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(self.data.data['Год'], self.data.data['Население'], marker='o', label='Фактическое население')


    pass
