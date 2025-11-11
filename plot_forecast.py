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
                    # Прогноз
        forecast_years = 5
        forecast = self.data.moving_average_forecast(years=forecast_years)
        last_year = self.data.data['Год'].iloc[-1]
        forecast_years_range = [last_year + i + 1 for i in range(forecast_years)]
        ax.plot(forecast_years_range, forecast, marker='o', linestyle='--', color='red', label='Прогноз')



    pass
