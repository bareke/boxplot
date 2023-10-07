import math

import pandas as pd
from fake_data import FakeData
from statistics import StatisticsRaw
from table import Table
from print_plot import PrintPlot


if __name__ == '__main__':
    min_value = 1
    max_value = 70
    limit_value = 4

    #! Datos generados
    fake_data = FakeData()
    # data = fake_data.generate_data(min_value, max_value, limit_value)
    data = fake_data.load_data_pre('data.txt')
    # print('Datos falsos', data, '\n')

    #! Calculo estadistico
    estadistic_raw = StatisticsRaw()
    data_calculate_raw = estadistic_raw.calculate_data(data)

    print('Calculos estadisticos')
    for key, value in data_calculate_raw.items():
        print(f'{key}: {value}')
    print()

    #! Tabla
    partitions=int(1+3.32*math.log10(limit_value))
    range_data = max(data)-min(data)
    amplitude = range_data/partitions
    interval = min(data)

    table = Table(partitions, amplitude)
    data_table = table.create_table(data, partitions, interval, amplitude, limit_value)
    print('Data frame')
    print(pd.DataFrame(data_table))

    #! Renderizar histograma
    print_plot = PrintPlot()
    print_plot.generate_plot(data)
