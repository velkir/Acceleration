import os

from OHLCDataManager import OHLCDataManager
from OHLCLocalMapperDF import OHLCLocalMapperDF
from OHLCLocalSource import OHLCLocalSource


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

