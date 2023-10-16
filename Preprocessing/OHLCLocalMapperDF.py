from Preprocessing.AbstractOHLCDataMapper import AbstractOHLCDataMapper


class OHLCLocalMapperDF(AbstractOHLCDataMapper):
    def map_data(self, raw_data):
        """Т.к. приходит в df формате, то ничего дополнительно делать не требуется"""
        # bars = raw_data[['open', 'high', 'low', 'close', 'timestamp']]
        bars = raw_data[['open', 'high', 'low', 'close', 'timestamp']].reset_index()
        bars.rename(columns={'index': 'id'}, inplace=True)

        return bars
