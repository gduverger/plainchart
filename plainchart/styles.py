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
