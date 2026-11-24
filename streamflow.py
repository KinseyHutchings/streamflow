# Code Block 1: Import methods
import matplotlib.pyplot as plt
import numpy as np
from datetime import date


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    provo_riv_array = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)

    dates = provo_riv_array[:, 0].astype("datetime64[s]")           # AI: sets the dates to a specific datetime format with seconds precision
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
    # Save the plot to a file before displaying it
    plt.savefig("provo_river_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, y_1, y_2, y_3, y_4, y_5 = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, y_1, y_2, y_3, y_4, y_5)


# Create a summary report of the streamflow data
# Excel: maximum for 10163000 is 131 & the mean is 56.95
def summarize(dates, flows, sites):
    """Print and save the maximum, minimum, and average flow for each gauge."""
    print(f"{'Gauge':<12}{'Max (cfs)':<12}{'Date of max':<22}{'Min (cfs)':<12}{'Avg (cfs)':<12}")       # AI: this f-string format separates each table header followed by a colon indicating the number of characters wanting to be preserved for each column

    with open("streamflow_summary.csv", "w", newline="") as file:           # AI: newline tells Python to not automatically convert line-ending characters when writing to this file
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")     # AI: this line is written to the CSV file as the header row, with each column separated by a comma

        for i, site in enumerate(sites):                                            # AI: loops through each site to determine the maximum, minimum, and average flow for each gauge
            gauge_flows = flows[:, i]
            maximum = np.max(gauge_flows)
            maximum_index = np.argmax(gauge_flows)                                  # stores the index to the maximum flow for the gauge
            maximum_date = np.datetime_as_string(dates[maximum_index], unit="m")    # AI: formats the date at the index to the minute (unit="m")
            maximum_date = maximum_date.replace("T", " ")                           # AI: replaces the "T" between the date and time with a space
            minimum = np.min(gauge_flows)
            average = np.mean(gauge_flows)

            print(
                f"{site:<12}{maximum:<12.1f}{maximum_date:<22}"                    # AI: formats the number of characters for each column item to be less than the stated number
                f"{minimum:<12.1f}{average:<12.1f}"
            )
            file.write(
                f"{site},{maximum:.1f},{maximum_date},{minimum:.1f},{average:.1f}\n"    # AI: write each of the gauge statistics to the CSV file following the same format as above
            )


flows = np.column_stack((y_1, y_2, y_3, y_4, y_5))      # AI: column stack combines five separate 1D arrays into one 2D array called flows
summarize(dates, flows, sites)


# Ask the user for a threshold water level
threshold = float(input("Enter a threshold water level (cfs): "))       # AI: asks the user to input the threshold water level in cfs

# For each gauge, find and print the number of hours in June 2021 when the flow was above the threshold
for i, site in enumerate(sites):                                            # AI: iterates through each site to calculate the hours above the threshold
    gauge_flows = flows[:, i]
    measurements_above_threshold = np.sum(gauge_flows > threshold)       # AI: counts the number of gauge_flow measurements above the threshold
    hours_above_threshold = measurements_above_threshold * 0.25          # AI: converts the number of measurements to hours (time is measured in 15-minute intervals)
    print(f"Site {site}: {hours_above_threshold} hours above threshold")  # AI: prints the number of hours above the threshold for each site