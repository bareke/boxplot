import pandas as pd
import matplotlib.pyplot as plot

pd.set_option('display.float_format', str)


class PrintPlot:
    def generate_plot(self, data: list) -> None:
        data = [float(item) for item in data]
        histogram  = pd.Series(data)

        min_value = int(min(data))
        max_value = int(min(data))

        interval = range(min_value, max_value + 2)

        histogram.plot.hist(bins=8, color='#F2AB6D', rwidth=0.85)

        plot.xticks(interval)
        plot.ylabel('Frecuencia')
        plot.xlabel('Edades')
        plot.title('Histograma')
        plot.savefig('plot.png')
