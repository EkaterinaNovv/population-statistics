class PopulationData:
    """Класс для хранения и обработки данных о населении"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
        self.data['Прирост, %'] = self.data['Население'].pct_change() * 100
