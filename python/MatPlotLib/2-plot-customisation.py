import matplotlib.pyplot as plt
import numpy as np

x = np.array[2023, 2024, 2025, 2026]
y = np.array[15, 25, 30, 20]
y2 = np.array[20, 60, 29, 20]
y3 = np.array[60, 30, 52, 20]

plt.plot(x, y, marker = ".", # This keyword argument creates a marker at each given point
               markersize = 10, # This keyword argument changes the size of the marker
               markerfacecolor = "white", # This keyword argument changes the colour of the marker
               markeredgecolor = "black", # This keyword argument changes the colour of the marker's edges
               linestyle = "dashdot", # This keyword argument changes the style of the line
               linewidth = 2, # This keyword argument changes the width of the line
               color = "red", # This keyword argument changes the colour of the line
               )

# Dictionary

line_style = dict( # You can use dictionaries to store the keyword arguments in order to use them in multiple locations
               marker = ".", # This keyword argument creates a marker at each given point
               markersize = 10, # This keyword argument changes the size of the marker
               markerfacecolor = "white", # This keyword argument changes the colour of the marker
               markeredgecolor = "black", # This keyword argument changes the colour of the marker's edges
               linestyle = "dashdot", # This keyword argument changes the style of the line
               linewidth = 2, # This keyword argument changes the width of the line
               color = "red", # This keyword argument changes the colour of the line
               )

plt.plot(x, y2, **line_style) # To use the dictionary, you need to have ** before the name
plt.plot(x, y3, color = "blue", **line_style) # Any keyword arguments within the plot function overwrites the ones in the dictionary 

plt.show()