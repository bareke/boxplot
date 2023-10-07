class Table:
    def __init__(self, partitions: int, amplitude: int):
        self.partitions = partitions
        self.amplitude = amplitude

    def create_table(self, data: list, partitions, interval: int, amplitude: int, limit_value: int) -> dict:
        result = []
        frecuencia_acomulada = 0
        frecuencia_relativa = 0
        frecuencia_relativa_acomulada = 0
        # Recorrido del for hasta n particiones
        for i in range(partitions):
            frecuencia_absoluta = 0
            interval = interval + amplitude
            marca = ((interval-amplitude)+interval) / 2
            # Recorrer la lista y mirar si esta dentro del intervalo y obtener la frecuencia absoluta
            if (i==partitions-1):
                for j in data:
                    if (j >= (interval-amplitude) and j <= interval):
                        frecuencia_absoluta += 1
            else:
                for j in data:
                    if (j>=(interval-amplitude) and j<interval):
                        frecuencia_absoluta += 1

            frecuencia_acomulada += frecuencia_absoluta
            frecuencia_relativa = frecuencia_absoluta/limit_value
            frecuencia_relativa_acomulada += frecuencia_relativa

            item = {
                'Intervalo': str(interval-amplitude)+" - "+str(interval),
                'Marca_De_Clase': marca,
                'Frecuencia_Absoluta': frecuencia_absoluta,
                'Frecuencia_Absoluta_Acomulada': str("{:.1f}".format(frecuencia_acomulada))+" - "+str("{:.1f}".format(frecuencia_relativa*100))+"%",
                'Frecuencia_Relativa': frecuencia_relativa,
                'Frecuencia_Relativa_Acomulada': str("{:.1f}".format(frecuencia_relativa_acomulada))+" - "+str("{:.1f}".format(frecuencia_relativa_acomulada*100))+"%",
            }
            result.append(item)

        return result
