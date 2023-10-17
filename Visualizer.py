import pandas as pd
import mplfinance as mpf
import numpy as np

class Visualizer:
    def __init__(self, bars, serialized_structure):
        self.bars = bars
        self.serialized_structure = serialized_structure

    def prepare_addplot(self, trends, bars):
        lines = []
        for trend in trends:
            x_values = pd.date_range(start=pd.Timestamp(trend['point0']['timestamp']),
                                     end=pd.Timestamp(trend['point1']['timestamp']),
                                     freq='T')
            y_values = np.linspace(trend['point0']['price'], trend['point1']['price'], len(x_values))
            df_line = pd.DataFrame(index=x_values, data={'price': y_values})
            aligned = bars.join(df_line, how='left')['price']
            lines.append(mpf.make_addplot(aligned, panel=0, color='r', secondary_y=False))
            lines.extend(self.prepare_addplot(trend['subtrends'], bars))
        return lines

    def plot(self):
        # Assuming bars and serialized_structure are defined
        self.bars['timestamp'] = pd.to_datetime(self.bars['timestamp'])
        self.bars.set_index('timestamp', inplace=True)

        # Prepare the trend lines to be added to the OHLC chart
        add_plots = self.prepare_addplot(self.serialized_structure['structure'], self.bars)

        # Plotting
        mpf.plot(self.bars, type='candle', style='charles', addplot=add_plots)
