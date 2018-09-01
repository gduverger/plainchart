
class PlainChart(object):


	def __init__(self, values, height=10, style=None):

		if height <= 0:
			raise PlainChartException('height must be above zero')

		self.values = values
		self.height = height 
		self.max = max(values)

		columns = []
		for value in self.values:

			cells = []
			for y in range(1, self.height + 1):

				if style:
					cell = style(self, value, y)

				else:
					cell = PlainChart.bar(self, value, y)

				cells.append(cell)

			columns.append(cells)

		# transpose and flip
		self.rows = list(reversed(list(map(list, zip(*columns)))))


	def y(self, value):
		_y = round(value * self.height / self.max) if self.max != 0 else 0
		return _y if _y <= self.height else self.height


	@staticmethod
	def bar(chart, value, y):
		return '▌' if y <= chart.y(value) else ' '


	@staticmethod
	def scatter(chart, value, y):
		return '×' if y == chart.y(value) else ' '


	def render(self, new_line='\n'):
		return new_line.join([''.join(row) for row in self.rows])


class PlainChartException(Exception):

	def __init__(self, message):
		self.message = message
