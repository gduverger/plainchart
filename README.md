PlainChart
==========

A simple plain-text, no-dependencies, `pip`-installable, open-source charting utility in Python.

Usage:
```python
>>> import plainchart
>>> chart = plainchart.PlainChart([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) # 🥧
>>> print(chart.render())

     ▌     ▌
     ▌     ▌
     ▌     ▌
     ▌ ▌   ▌
    ▌▌ ▌▌ ▌▌
    ▌▌ ▌▌ ▌▌
  ▌ ▌▌ ▌▌ ▌▌
▌ ▌ ▌▌ ▌▌▌▌▌
▌ ▌ ▌▌▌▌▌▌▌▌
▌▌▌▌▌▌▌▌▌▌▌▌
```

Installation
------------

To install PlainChart, you can use [pipenv](http://pipenv.org/) or pip:
```bash
$ pipenv install plainchart
```

Features
--------

With PlainChart, you can:
- render an array of values in a plain text chart
- limit the height of the chart and have the values rendered accordingly
- render a different style of chart, e.g., `plainchart.PlainChart.bar` or `plainchart.PlainChart.scatter`
- implement your own style of chart, e.g., `mean_html` (see example below)

Examples
--------

```python
>>> import plainchart
>>> import random
>>>
>>> values = [random.randint(0, 10) for _ in range(100)]
>>> chart = plainchart.PlainChart(values)
>>>
>>> print(chart.render())

        ▌   ▌       ▌   ▌                         ▌                      ▌        ▌        ▌
  ▌     ▌   ▌   ▌▌  ▌   ▌  ▌                      ▌                   ▌  ▌        ▌        ▌
  ▌     ▌   ▌▌  ▌▌  ▌   ▌  ▌▌                     ▌   ▌    ▌▌  ▌   ▌  ▌  ▌     ▌  ▌    ▌   ▌       ▌
  ▌ ▌  ▌▌   ▌▌  ▌▌▌ ▌  ▌▌ ▌▌▌                 ▌   ▌   ▌    ▌▌  ▌  ▌▌  ▌  ▌   ▌ ▌  ▌  ▌ ▌   ▌       ▌
  ▌ ▌  ▌▌▌  ▌▌  ▌▌▌ ▌▌ ▌▌ ▌▌▌▌   ▌         ▌  ▌   ▌   ▌    ▌▌  ▌  ▌▌  ▌  ▌   ▌ ▌ ▌▌▌ ▌ ▌   ▌       ▌
  ▌ ▌  ▌▌▌  ▌▌  ▌▌▌ ▌▌ ▌▌ ▌▌▌▌   ▌▌        ▌  ▌   ▌ ▌ ▌    ▌▌  ▌  ▌▌  ▌ ▌▌   ▌ ▌▌▌▌▌▌▌ ▌▌▌ ▌       ▌
  ▌ ▌  ▌▌▌  ▌▌  ▌▌▌ ▌▌ ▌▌▌▌▌▌▌▌▌ ▌▌▌    ▌  ▌  ▌ ▌ ▌ ▌ ▌ ▌  ▌▌  ▌  ▌▌  ▌ ▌▌   ▌ ▌▌▌▌▌▌▌ ▌▌▌ ▌▌     ▌▌
  ▌ ▌ ▌▌▌▌ ▌▌▌ ▌▌▌▌ ▌▌▌▌▌▌▌▌▌▌▌▌ ▌▌▌  ▌ ▌  ▌  ▌ ▌▌▌ ▌ ▌ ▌▌ ▌▌▌ ▌  ▌▌▌ ▌ ▌▌   ▌▌▌▌▌▌▌▌▌ ▌▌▌ ▌▌   ▌ ▌▌
 ▌▌▌▌ ▌▌▌▌ ▌▌▌ ▌▌▌▌ ▌▌▌▌▌▌▌▌▌▌▌▌ ▌▌▌ ▌▌ ▌  ▌  ▌▌▌▌▌▌▌ ▌▌▌▌▌▌▌▌ ▌▌ ▌▌▌▌▌ ▌▌▌▌ ▌▌▌▌▌▌▌▌▌ ▌▌▌ ▌▌▌  ▌▌▌▌
▌▌▌▌▌ ▌▌▌▌ ▌▌▌▌▌▌▌▌ ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ ▌▌ ▌ ▌▌  ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ ▌▌▌▌▌▌▌▌▌▌▌▌▌▌ ▌▌▌▌▌▌▌▌▌▌▌▌▌
```

```python
>>> import plainchart
>>> import math
>>> import numpy as np
>>>
>>> values = [1.3 + math.sin(x) for x in np.linspace(0, 4 * math.pi, num=100)]
>>> chart = plainchart.PlainChart(values, style=plainchart.PlainChart.scatter)
>>>
>>> print(chart.render())

         ××××××××                                          ×××××××
      ×××        ×××                                    ×××       ×××
    ××              ××                               ×××             ××
  ××                  ××                            ×                  ××
××                      ××                        ××                     ××                        ×
                          ×                     ××                         ××                    ××
                           ××                 ××                             ××                ××
                             ×××            ××                                 ××            ××
                                ×××     ××××                                     ××××    ××××
                                   ×××××                                             ××××
```

You can also implement your own style of chart. Below is an example of a HTML chart (`mean_html.py`) with different colors for values below and above the mean.

```python
import plainchart
import random
import statistics

def mean_html(chart, value, y):
	mean = statistics.mean(chart.values)
	mean_y = chart.y(mean)
	value_y = chart.y(value)

	if value_y <= mean_y:

		if y <= value_y:
			return '<span style="color:green">▌</span>'

		return '<span style="color:white">▌</span>'

	else:

		if y <= mean_y:
			return '<span style="color:green">▌</span>'

		elif y <= value_y:
			return '<span style="color:red">▌</span>'

		return '<span style="color:white">▌</span>'

values = [random.randint(0, 10) for _ in range(100)]
chart = plainchart.PlainChart(values, style=mean_html)

print(chart.render(new_line='<br>'))
```

```bash
$ python mean_html.py > mean.html
```

![Mean HTML chart](https://github.com/gduverger/plainchart/blob/master/static/mean.png "Mean HTML chart")

Contribute
----------

Please feel free to open an issue to propose a new feature or point out a bug. You can also fork the PlainChart repository and submit a pull request.

Support
-------

PlainChart is free and under the [MIT License](LICENSE). To support its development, you can make a donation to [cash.me/$gduverger](https://cash.me/$gduverger).
