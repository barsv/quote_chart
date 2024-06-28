# Live example

https://colab.research.google.com/drive/1GQ5Vuf07_8WYIYhDSsZxZc4f7fWaZPFP

# What is it for?

Sometimes I need to plot something on top of candlestick prices in my Jupyter notebooks. The problem with matplotlib/mplfinance or plotly is that out of the box, they don't work well when the size of the data is more than 10k points. They can plot it, but the inconvenience is that zoom/pan becomes slow.

10k points is just a week of 1-minute candles. But sometimes I want to explore data for a year. The solution I see is to automatically slice and resample the DataFrame based on the current zoom/pan position. I haven't found a simpler way to do this than to write this small library.

If someone knows an easier way to achieve the same, then please let me know by creating an issue.

This library is far from perfect. There are known bugs that I don't have time to fix. But so far, it's better than nothing for me.

# Features

Basically, I was trying to make it similar to the UX on TradingView, but not everything was easy to implement. So I implemented what I could/had time for:

- Zoom by scrolling with the right side fixed by default.
- Zoom at the cursor position via Ctrl + scroll.
- Pan by scrolling via Shift + scroll.
- Current cursor position coordinates.
- Spike across all subplots (spike is a vertical line at the cursor position).
- Period buttons to change the resampling period.

# Installation

```bash
!pip install quote_chart
```

Once installed, you need to create an instance of a Dash app by calling the `create_chart_app` function and passing it at least one parameter - the function that will create a Plotly figure for the currently visible X range given by `x0, x1` parameters. Here is a minimal working example:

```python
from quote_chart import create_chart_app
import plotly.express as px

def create_figure(x0, x1):
    df = px.data.stocks()  # Sample data in plotly.express
    # Without indexing by date, it will not put dates on the x-axis.
    df.set_index('date', inplace=True)
    return px.line(df['GOOG'])  # Plot GOOG dummy price as a line.

app = create_chart_app(create_figure)
app.run_server()
```

## Usage without installation

The library code is just in one file `quote_chart.py`, so you can just drop it into the same folder with your Jupyter notebook and import it via `from quote_chart import create_chart_app`. In this case, you will need to manually install dependencies:

```bash
!pip install dash plotly pandas 'numpy<2.0.0'
```

# Examples

There are 3 examples:

- `example_min.ipynb` - This is the minimal example of how to use quote_chart. This example doesn't showcase rescaling/period selection, which is the main feature. Available in Google Colab [here](https://colab.research.google.com/drive/1QfUZVpDA6lzIqXmUFGNXZ_fnvsBonJvk).

- `example_random.ipynb` - A better example of the use of quote_chart. It has period selection and resampling logic. But it has random data and doesn't have technical analysis charts in it. Available in Google Colab [here](https://colab.research.google.com/drive/1mIf-MKeGpvWILqzxiWCY_oIwIRPDE9Hy).

- `example_BTCUSDT.ipynb` - This is a real-world example with MACD and exponential moving average added to the chart. The only thing that I don't like in this example is that it gets data from Binance, and I'm not sure if it will work in the future. Available in Google Colab [here](https://colab.research.google.com/drive/1GQ5Vuf07_8WYIYhDSsZxZc4f7fWaZPFP).
