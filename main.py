import os

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


from DataWalker import DataWalker
from Preprocessing.OHLCDataManager import OHLCDataManager
from Preprocessing.OHLCLocalMapperDF import OHLCLocalMapperDF
from Preprocessing.OHLCLocalSource import OHLCLocalSource
from Serializer import Serializer
from Visualizer import Visualizer


def get_first_filename(directory_path):
    try:
        filenames = os.listdir(directory_path)
        csv_filenames = [filename for filename in filenames if filename.endswith('.csv')]
        first_csv_filename = csv_filenames[0]
        return first_csv_filename
    except Exception as e:
        return str(e)

directory_path = "ohlc_data/"
path = directory_path+get_first_filename(directory_path)
print(path)


directory_path = "ohlc_data/"
ohlc_source = OHLCLocalSource()
ohlc_mapper = OHLCLocalMapperDF()
ohlc_data_manager = OHLCDataManager(ohlc_data_source=ohlc_source, ohlc_data_mapper=ohlc_mapper,
                                    path=path)

bars = ohlc_data_manager.prepare_ohlc_data()

print(bars)

data_walker = DataWalker(ohlc_data=bars)
for bar in range(bars.shape[0]):
    print(f"Current bar: {bar}")
    data_walker.next()

print("Completed!")

serializer = Serializer()
serialized_structure = serializer.structure_to_dict(data_walker.structure)
print(serialized_structure)

visualizer = Visualizer(bars=bars, serialized_structure=serialized_structure)
visualizer.plot()








