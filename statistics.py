import pandas as pd

pd.set_option('display.float_format', str)


class StatisticsRaw:
    def calculate_data(self, data: list) -> dict:
        df = pd.DataFrame({'data': data})
        statistic = {
            'media': df['data'].mean(),
            'mediana': df['data'].median(),
            'moda': df['data'].mode().values[0],
            'primer_cuartil': df['data'].quantile(0.25),
            'segundo_cuartil': df['data'].quantile(0.5),
            'tercer_cuartil': df['data'].quantile(0.75),
            'raro_cuartil': df['data'].quantile(.63),
        }

        return statistic
