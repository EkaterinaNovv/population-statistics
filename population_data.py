import pandas as pd

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
