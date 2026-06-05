import unittest
import time_series_visualizer
import matplotlib as mpl
import pandas as pd

class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.df = time_series_visualizer.df

    def test_data_import(self):
        self.assertEqual(type(self.df), pd.core.frame.DataFrame, "Expected data to be imported into a pandas DataFrame.")
        self.assertEqual(self.df.index.name, 'date', "Expected the index column to be named 'date'.")

    def test_data_cleaning(self):
        actual_rows = len(self.df)
        expected_rows = 1238 # Standard count after removing top 2.5% and bottom 2.5% anomalies
        self.assertEqual(actual_rows, expected_rows, f"Expected filtered data rows to be {expected_rows}.")

    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertIsInstance(fig, mpl.figure.Figure, "Expected line plot to return a matplotlib figure object.")
        ax = fig.get_axes()[0]
        self.assertEqual(ax.get_title(), 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019', "Line plot title is incorrect.")
        self.assertEqual(ax.get_xlabel(), 'Date', "Line plot X-axis label should be 'Date'.")
        self.assertEqual(ax.get_ylabel(), 'Page Views', "Line plot Y-axis label should be 'Page Views'.")

    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertIsInstance(fig, mpl.figure.Figure, "Expected bar plot to return a matplotlib figure object.")
        ax = fig.get_axes()[0]
        self.assertEqual(ax.get_xlabel(), 'Years', "Bar plot X-axis label should be 'Years'.")
        self.assertEqual(ax.get_ylabel(), 'Average Page Views', "Bar plot Y-axis label should be 'Average Page Views'.")
        
    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertIsInstance(fig, mpl.figure.Figure, "Expected box plot to return a matplotlib figure object.")
        axes = fig.get_axes()
        self.assertEqual(len(axes), 2, "Expected two adjacent box subplots.")
        self.assertEqual(axes[0].get_title(), 'Year-wise Box Plot (Trend)', "First box plot title is incorrect.")
        self.assertEqual(axes[1].get_title(), 'Month-wise Box Plot (Seasonality)', "Second box plot title is incorrect.")

if __name__ == "__main__":
    unittest.main()
