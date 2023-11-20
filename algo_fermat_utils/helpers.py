import time
import psutil


def measure_performance(func):
    def wrapper(*args, **kwargs):
        # Check if this is the first call
        if not hasattr(wrapper, 'call_count'):
            wrapper.call_count = 0
            wrapper.start_time = time.perf_counter()
            wrapper.start_cpu_times = psutil.Process().cpu_times()

        wrapper.call_count += 1

        # Execute the function
        result = func(*args, **kwargs)

        wrapper.call_count -= 1
        if wrapper.call_count == 0:
            # Record the end time and CPU usage
            end_time = time.perf_counter()
            end_cpu_times = psutil.Process().cpu_times()

            # Calculate the elapsed time and CPU usage
            elapsed_time = end_time - wrapper.start_time
            elapsed_cpu_times_user = end_cpu_times.user - wrapper.start_cpu_times.user
            elapsed_cpu_times_system = end_cpu_times.system - wrapper.start_cpu_times.system

            # Print the performance metrics
            print("+-------------------+------------+")
            print("| Metric            | Value      |")
            print("+-------------------+------------+")
            print(f"| Execution time    | {elapsed_time:.6f} s |")
            print(f"| User CPU time     | {elapsed_cpu_times_user:.6f} s |")
            print(f"| System CPU time   | {elapsed_cpu_times_system:.6f} s |")
            print(f"| Memory usage      | {psutil.Process().memory_info().rss / 1024 / 1024:.4f} MB |")
            print("+-------------------+------------+")

        return result

    return wrapper
