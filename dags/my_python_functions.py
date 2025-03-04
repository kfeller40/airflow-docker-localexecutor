from datetime import datetime
import time

def print_date():
    print(f"Current date and time: {datetime.now()}")

def sleep():
    time.sleep(5)

def echo_hello():
    print("Hello, Airflow!")

import csv
from datetime import datetime

def create_time_csv_sample():

# Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Specify the directory inside the Docker container
    directory = "/app"  # This is a common directory used in Docker containers

    # Create a CSV file named with the current time in the specified directory
    file_name = f"{directory}/{current_time}.csv"

    # Write the current time inside the file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Current Time"])
        writer.writerow([current_time])

    print(f"CSV file '{file_name}' created with the current time inside.")