import matplotlib.pyplot as plt
import numpy as np

x = np.array[2023, 2024, 2025, 2026]
y1 = np.array[15, 25, 30, 20]
y2 = np.array[20, 60, 29, 20]
y3 = np.array[60, 30, 52, 20]

plt.title("Class Size", # This puts a title above the plotted graphs
           fontsize = 20, # This keyword argument changes the fontsize of the title
           family = "Ariel", # This keyword argument changes the font family of the title
           fontweight = "bold", # This keyword argument changes the thickness of the text in the title
           color = "red" # This keyword argument chanegs the colour of the title
           )

plt.xlabel("Year", # This puts a label on the x-axis
           fontsize = 20,
           family = "Ariel",
           fontweight = "bold", 
           color = "red" 
           )    

plt.ylabel("Students", # This puts a label on the y-axis
           fontsize = 20,
           family = "Ariel",
           fontweight = "bold", 
           color = "red" 
           )

plt.tick_params(axis="both", # This allows you to edit the ticks on the axis
                color = "red")

plt.plot[x, y1]
plt.plot[x, y2]
plt.plot[x, y3]

plt.xticks(x) # This makes it so the are only ticks at the given values

plt.show()