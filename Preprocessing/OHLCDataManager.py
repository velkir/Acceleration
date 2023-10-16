import datetime
from Preprocessing.AbstractOHLCDataMapper import AbstractOHLCDataMapper
from Preprocessing.AbstractOHLCDataSource import OHLCDataSource


class OHLCDataManager:
    def __init__(self, path, ohlc_data_source: OHLCDataSource, ohlc_data_mapper: AbstractOHLCDataMapper):
        self.ohlc_data_source = ohlc_data_source
        self.ohlc_data_mapper = ohlc_data_mapper
        self.ohlc_data = None
        self.path = path

    def _get_ohlc_data(self):
        start = datetime.datetime.now()
        print(f"Начало взятия в pd: {start}")
        ohlc_data = self.ohlc_data_source.get_raw_ohlc_data(path=self.path)
        end = datetime.datetime.now()
        print(f"Окончание взятия в pd: {end}")
        print(f"Итоговое время: {end-start}")
        return ohlc_data

    def _map_ohlc_data(self, temp_data):
        start = datetime.datetime.now()
        print(f"Начало маппинга: {start}")
        self.ohlc_data = self.ohlc_data_mapper.map_data(raw_data=temp_data)
        end = datetime.datetime.now()
        print(f"Окончание маппинга: {end}")
        print(f"Итоговое время: {end-start}")

    def prepare_ohlc_data(self):
        temp_data = self._get_ohlc_data()
        self._map_ohlc_data(temp_data)
        return self.ohlc_data if self.ohlc_data is not [] else "Something went wrong, empty ohlc_data!"
