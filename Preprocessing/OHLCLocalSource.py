import pandas as pd
from Preprocessing.AbstractOHLCDataSource import OHLCDataSource


class OHLCLocalSource(OHLCDataSource):
    def get_raw_ohlc_data(self, path):
        return pd.read_csv(path)
