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

This lib is far from perfect, there are known bugs, but so far it's better than
nothing for me.

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

I actually recommend to just drop the file quote_chart.py into the same folder
with jupyter notebook and import via `from quote_chart import create_chart_app`.

But I will try to add it to PyPi.

Once imported you need to create an example of Dash app by making a call to the
function create_chart_app and pass it at least one parameter - the function that
will create a plotly figure for currently visisble X range that is given by x0,
x1 parameters. Here is the minimal working example:

```
from quote_chart import create_chart_app
import plotly.express as px

def create_figure(x0, x1):
    df = px.data.stocks()
    df.set_index('date', inplace=True)
    return px.line(df['GOOG'])

app = create_chart_app(create_figure)
app.run_server()
```

# Examples

There are 3 examples:

- example_min.ipynb - This is the minimal example of how to use quote_chart.
This example doesn't showcase rescaling/period selection that is the main
feature.

- example_random.ipynb - A better example of the use of quote_chart. It has
period selection and resampling logic. But it has random data and doesn't have
technical analysis charts in it.

- example_BTCUSDT.ipynb - This is a realworld example with MACD and exponential
moving average added to the chart. The only thing that I don't like in this
example is that it gets data from binance and I'm not sure if it will work in
future.

I hope that I will find time to put it into colab.