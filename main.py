import time_series_visualizer
from unittest import main

# Test functions by generating and saving the plots
print("Generating Line Plot...")
time_series_visualizer.draw_line_plot()

print("Generating Bar Plot...")
time_series_visualizer.draw_bar_plot()

print("Generating Box Plots...")
time_series_visualizer.draw_box_plot()

# Run the automated testing module
print("\nRunning automated unit tests...")
main(module='test_module', exit=False)
