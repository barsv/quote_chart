# Live example

https://colab.research.google.com/drive/1GQ5Vuf07_8WYIYhDSsZxZc4f7fWaZPFP

# What is it for?

Sometimes I need to plot something on top of candlestick prices in my jupyter
notebooks. The problem with matplotlib/mplfinance or plotly is that out of the
box they don't work well when the size of the data is more than 10k points. I
mean that they can plot it but the inconvenience is that zoom/pan is slow.

10k points is just a week of 1 minute candles. But sometimes I wan't to explore
data for a year. The solution I see is to automatically slice and resample the
dataframe based on the current zoom/pan position. I haven't found a simplier way
to do this than to write this small lib.

If someone knows an easier way to achive the same then please let me know by
creating an issue.

This lib is far from perfect. There are known bugs that I don't have time to
fix. But so far it's better than nothing for me.

# Features

Basically I was trying to do it similar to UX on trading view but not everything
was easy to implement. So I implemented what I could/had time for.

- zoom by scroll with right side fixed by default.
- zoom at the cursor position via Ctrl+scroll.
- pan by scroll via Shift+scroll.
- current cursor position coordinates.
- spike across all subplots (spike is vetical line at the cursor position).
- period buttons to change resampling period.

# Installation

```
!pip install quote_chart
```

Once installed you need to create an instance of a Dash app by making a call to
the function create_chart_app and pass it at least one parameter - the function
that will create a plotly figure for currently visisble X range that is given by
x0, x1 parameters. Here is the minimal working example:

```
from quote_chart import create_chart_app
import plotly.express as px

def create_figure(x0, x1):
    df = px.data.stocks() # sample data in plotly.express.
    # without index by date it will not put dates on the x axis.
    df.set_index('date', inplace=True) 
    return px.line(df['GOOG']) # plot GOOG dummy price as a line.

app = create_chart_app(create_figure)
app.run_server()
```

## Usage without installation

The lib code is just in one file quote_chart.py so you can just drop it
into the same folder with your jupyter notebook and import via `from quote_chart
import create_chart_app`. In this case though you will need to manually install
dependencies:

```
!pip install dash plotly pandas 'numpy<2.0.0'
```


# Examples

There are 3 examples:

- example_min.ipynb - This is the minimal example of how to use quote_chart.
This example doesn't showcase rescaling/period selection that is the main
feature. Available in google colab [here](
https://colab.research.google.com/drive/1QfUZVpDA6lzIqXmUFGNXZ_fnvsBonJvk).

- example_random.ipynb - A better example of the use of quote_chart. It has
period selection and resampling logic. But it has random data and doesn't have
technical analysis charts in it. Available in google colab [here](
https://colab.research.google.com/drive/1mIf-MKeGpvWILqzxiWCY_oIwIRPDE9Hy).

- example_BTCUSDT.ipynb - This is a realworld example with MACD and exponential
moving average added to the chart. The only thing that I don't like in this
example is that it gets data from binance and I'm not sure if it will work in
future. Available in google colab [here](
https://colab.research.google.com/drive/1GQ5Vuf07_8WYIYhDSsZxZc4f7fWaZPFP).
