# CPU Usage Monitor

This Python script monitors and plots the CPU usage in real-time.

## Dependencies

The script requires the following Python libraries:
- `psutil`: for retrieving system information such as CPU usage.
- `time`: for working with time-related functions.
- `matplotlib.pyplot`: for creating the plot.

You can install these dependencies using pip:

```bash
pip install psutil matplotlib

# How It Works
The script defines a function monitor_cpu_usage() that monitors the CPU usage and plots it in real-time. Here’s a brief overview of what the function does:

Initializes two lists, cpu_percentages and timestamps, to store the CPU usage values and the corresponding timestamps, respectively.
Sets up a plot with ‘Time’ as the x-axis and ‘CPU Usage (%)’ as the y-axis.
In a loop that runs 20 times, it:
Retrieves the current CPU usage percentage using psutil.cpu_percent(interval=1).
Appends the CPU usage and the current timestamp to the respective lists.
If the number of data points exceeds 50, it removes the oldest data points to keep the total number at 50.
Plots the CPU usage percentages against the timestamps.
Pauses for a short interval to allow the plot to update.
Clears the previous plot to prepare for the next iteration.
The function is called in the main section of the script, so it runs automatically when you run the script.

Usage
To run the script, navigate to its directory and run the following command:

python cpu_usage_monitor.py

This will start the CPU usage monitor, and you should see a plot that updates in real-time.
