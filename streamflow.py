# Code Block 1: Import methods
import matplotlib.pyplot as plt
import numpy as np

### Part 3 - Provo River Streamflow Data


# You will now create a graph using streamflow data of the Provo River in June 2021.

### Numpy Array Creation & Slicing

# Create and slice the array to create the x and y-axis values. These will correspond to the following columns in the CSV linked on the HW instructions page:

   #y_1 - Site 10163000
   #y_2 - Site 10155200
   #y_3 - Site 10155500
   #y_4 - Site 10154200
   #y_5 - Site 10155000


# Code Block 5: Create an array and organize by columns
from datetime import date
# This code imports the Provo River CSV file into a 2D array
provo_riv_array = np.genfromtxt("June-2021-Provo-River-Streamflow-Rates.csv", delimiter=",", dtype=str, skip_header=1)

x = provo_riv_array[:, 0].astype("datetime64")    # AI reminded me that to get a column from an array, call the array name, copy the entire array, and then call the index number of the column
y_1 = provo_riv_array[:, 1].astype(float)   # Site 10163000
y_2 = provo_riv_array[:, 2].astype(float)   # Site 10155200
y_3 = provo_riv_array[:, 3].astype(float)   # Site 10155500
y_4 = provo_riv_array[:, 4].astype(float)   # Site 10154200
y_5 = provo_riv_array[:, 5].astype(float)   # Site 10155000

### Graphing the Data

# Plot x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.

# Code Block 6: Graph the Provo River data
plt.plot(x, y_1, label="10163000", color="purple")
plt.plot(x, y_2, label="10155200", color="teal")
plt.plot(x, y_3, label="10155500", color="green")
plt.plot(x, y_4, label="10154200", color="orange")
plt.plot(x, y_5, label="10155000", color="red")
plt.title("Provo River Streamflow Data (2021)")
plt.xlabel("Date")
plt.ylabel("Flowrate (cfs)")
plt.xticks(rotation=45)
plt.legend(title="Site Numbers", loc="upper right")
plt.grid()
plt.show()