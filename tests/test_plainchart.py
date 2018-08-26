import unittest
import plainchart


class TestPlainChart(unittest.TestCase):
	# python -m unittest tests.test_plainchart.TestPlainChart


	def test_init(self):
		# python -m unittest tests.test_plainchart.TestPlainChart.test_init

		with self.assertRaises(TypeError):
			# __init__() missing 1 required positional argument: 'values'
			chart = plainchart.PlainChart()

		with self.assertRaises(TypeError):
			# 'int' object is not iterable
			chart = plainchart.PlainChart(0)

		with self.assertRaises(ValueError):
			# max() arg is an empty sequence
			chart = plainchart.PlainChart([])

		chart = plainchart.PlainChart([0])
		self.assertEqual(chart.values, [0])
		self.assertEqual(chart.max, 0)

		chart = plainchart.PlainChart([1])
		self.assertEqual(chart.values, [1])
		self.assertEqual(chart.max, 1)

		chart = plainchart.PlainChart([1, 2])
		self.assertEqual(chart.values, [1, 2])
		self.assertEqual(chart.max, 2)

		chart = plainchart.PlainChart([-1, -2])
		self.assertEqual(chart.values, [-1, -2])
		self.assertEqual(chart.max, -1)

		chart = plainchart.PlainChart([-1, 1])
		self.assertEqual(chart.values, [-1, 1])
		self.assertEqual(chart.max, 1)

		values = list(range(0, 1000)) # [0, 999]
		chart = plainchart.PlainChart(values)
		self.assertEqual(chart.values, values)
		self.assertEqual(chart.max, 999)


	def test_height(self):
		# python -m unittest tests.test_plainchart.TestPlainChart.test_height

		with self.assertRaises(plainchart.PlainChartException):
			self.assertEqual(plainchart.PlainChart([0], height=-1).height, -1)

		with self.assertRaises(plainchart.PlainChartException):
			self.assertEqual(plainchart.PlainChart([0], height=0).height, 0)

		self.assertEqual(plainchart.PlainChart([0], height=1).height, 1)
		self.assertEqual(plainchart.PlainChart([0], height=1000).height, 1000)


	def test_y(self):
		# python -m unittest tests.test_plainchart.TestPlainChart.test_y
		values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

		chart = plainchart.PlainChart(values, height=5)
		self.assertEqual(chart.y(0), 0)
		self.assertEqual(chart.y(1), 0)
		self.assertEqual(chart.y(2), 1)
		self.assertEqual(chart.y(5), 2) # round
		self.assertEqual(chart.y(10), 5)

		chart = plainchart.PlainChart(values, height=10)
		self.assertEqual(chart.y(0), 0)
		self.assertEqual(chart.y(1), 1)
		self.assertEqual(chart.y(2), 2)
		self.assertEqual(chart.y(5), 5)
		self.assertEqual(chart.y(10), 10)

		chart = plainchart.PlainChart(values, height=20)
		self.assertEqual(chart.y(0), 0)
		self.assertEqual(chart.y(1), 2)
		self.assertEqual(chart.y(2), 4)
		self.assertEqual(chart.y(5), 10)
		self.assertEqual(chart.y(10), 20)


	def test_rows(self):
		# python -m unittest tests.test_plainchart.TestPlainChart.test_rows

		chart = plainchart.PlainChart([1, 2, 3], height=3)
		self.assertEqual(chart.rows, [
			[' ', ' ', '▌'],
			[' ', '▌', '▌'],
			['▌', '▌', '▌']])


	def test_style(self):
		# python -m unittest tests.test_plainchart.TestPlainChart.test_style

		chart = plainchart.PlainChart([1, 2, 3], height=3, style=plainchart.PlainChart.bar)
		self.assertEqual(chart.rows, [
			[' ', ' ', '▌'],
			[' ', '▌', '▌'],
			['▌', '▌', '▌']])

		chart = plainchart.PlainChart([1, 2, 3], height=3, style=plainchart.PlainChart.scatter)
		self.assertEqual(chart.rows, [
			[' ', ' ', '×'],
			[' ', '×', ' '],
			['×', ' ', ' ']])


	def test_render(self):
		# python -m unittest tests.test_plainchart.TestPlainChart.test_render

		chart = plainchart.PlainChart([1, 2, 3], height=3)
		self.assertEqual(chart.render(), '  ▌\n ▌▌\n▌▌▌')

		chart = plainchart.PlainChart([1, 2, 3], height=3)
		self.assertEqual(chart.render(new_line='<br>'), '  ▌<br> ▌▌<br>▌▌▌')


if __name__ == '__main__':
	unittest.main()
