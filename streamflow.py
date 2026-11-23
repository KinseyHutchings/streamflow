# Code Block 1: Import methods
import matplotlib.pyplot as plt
import numpy as np
from datetime import date


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    provo_riv_array = np.genfromtxt("June-2021-Provo-River-Streamflow-Rates.csv", delimiter=",", dtype=str, skip_header=1)

    dates = provo_riv_array[:, 0].astype("datetime64")    # AI reminded me that to get a column from an array, call the array name, copy the entire array, and then call the index number of the column
    y_1 = provo_riv_array[:, 1].astype(float)   # Site 10163000
    y_2 = provo_riv_array[:, 2].astype(float)   # Site 10155200
    y_3 = provo_riv_array[:, 3].astype(float)   # Site 10155500
    y_4 = provo_riv_array[:, 4].astype(float)   # Site 10154200
    y_5 = provo_riv_array[:, 5].astype(float)   # Site 10155000
    return dates, y_1, y_2, y_3, y_4, y_5

    
def plot_streamflow(dates, y_1, y_2, y_3, y_4, y_5):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.plot(dates, y_1, label="10163000", color="purple")
    plt.plot(dates, y_2, label="10155200", color="teal")
    plt.plot(dates, y_3, label="10155500", color="green")
    plt.plot(dates, y_4, label="10154200", color="orange")
    plt.plot(dates, y_5, label="10155000", color="red")
    plt.title("Provo River Streamflow Data (2021)")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.xticks(rotation=45)
    plt.legend(title="Site Numbers", loc="upper right")
    plt.grid()
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, y_1, y_2, y_3, y_4, y_5 = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, y_1, y_2, y_3, y_4, y_5)