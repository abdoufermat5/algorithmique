import time

import psutil


def measure_performance(func):
    def wrapper(*args, **kwargs):
        # Get the current process
        process = psutil.Process()

        # Record the start time and CPU usage
        start_time = time.perf_counter()
        start_cpu_times = process.cpu_times()

        # Execute the function
        result = func(*args, **kwargs)

        # Record the end time and CPU usage
        end_time = time.perf_counter()
        end_cpu_times = process.cpu_times()

        # Calculate the elapsed time and CPU usage
        elapsed_time = end_time - start_time
        elapsed_cpu_times_user = end_cpu_times.user - start_cpu_times.user
        elapsed_cpu_times_system = end_cpu_times.system - start_cpu_times.system

        # Print the performance metrics in a table format
        print("+-------------------+------------+")
        print("| Metric            | Value      |")
        print("+-------------------+------------+")
        print(f"| Execution time    | {elapsed_time:.6f} s |")
        print(f"| User CPU time     | {elapsed_cpu_times_user:.6f} s |")
        print(f"| System CPU time   | {elapsed_cpu_times_system:.6f} s |")
        print(f"| Memory usage      | {process.memory_info().rss / 1024 / 1024:.2f} MB |")
        print("+-------------------+------------+")

        return result

    return wrapper
