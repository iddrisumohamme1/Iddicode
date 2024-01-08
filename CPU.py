import psutil
import time
import matplotlib.pyplot as plt

def monitor_cpu_usage():
    cpu_percentages = []  # List to store CPU usage values
    timestamps = []  # List to store corresponding timestamps

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage Monitor')

    for i in range(20):
        cpu_percent = psutil.cpu_percent(interval=1)

        # Append CPU usage and timestamp to the lists
        cpu_percentages.append(cpu_percent)
        timestamps.append(time.time())

        # Limit the number of data points to display
        max_points = 50
        if len(cpu_percentages) > max_points:
            cpu_percentages = cpu_percentages[-max_points:]
            timestamps = timestamps[-max_points:]

        plt.plot(timestamps, cpu_percentages, 'b-')
        plt.gcf().autofmt_xdate()  # Format x-axis timestamps

        plt.pause(0.001)
        plt.clf()  # Clear the previous plot

if __name__ == '__main__':
    monitor_cpu_usage()

