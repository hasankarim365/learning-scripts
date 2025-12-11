import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [1, 10, 15, 20, 25]

plt.grid( # This creates grid lines
    axis = "both", # This keyword argument selects the axis where lines are to be shown 
    linewidth = 2, # This keyword argument changes the width of the grid lines
    color = "lightgray", # This keyword argument changes the color of the grid lines
    linestyle = "solid", # This keyword argument changes the style of the grid lines
) 


plt.plot(x, y)
plt.show()
plt.savefig()