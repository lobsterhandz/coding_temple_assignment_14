import os

def read_weather_data(file_name):
    # Change to the directory containing the file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Looking for file: {file_name}")
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist in the directory {os.getcwd()}.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def extract_temperatures(data_lines):
    temperatures = []
    for line in data_lines:
        date, temp = line.strip().split(',')
        temperature_value = int(temp.replace('°C', '').strip())
        temperatures.append(temperature_value)
    return temperatures

def calculate_average_temperature(temperatures):
    if len(temperatures) == 0:
        return 0
    return sum(temperatures) / len(temperatures)

def analyze_weather_data(file_names):
    yearly_averages = {}
    for file_name in file_names:
        year = file_name.split('_')[1].split('.')[0]
        data_lines = read_weather_data(file_name)
        temperatures = extract_temperatures(data_lines)
        average_temp = calculate_average_temperature(temperatures)
        yearly_averages[year] = average_temp
    return yearly_averages

def find_year_with_highest_average(yearly_averages):
    if not yearly_averages:
        return None, None
    highest_year = max(yearly_averages, key=yearly_averages.get)
    return highest_year, yearly_averages[highest_year]

# Example to analyze multiple files and find the year with the highest average temperature
file_names = ['weather_2020.txt', 'weather_2021.txt']
yearly_averages = analyze_weather_data(file_names)
highest_year, highest_avg = find_year_with_highest_average(yearly_averages)

print("Yearly Averages:", yearly_averages)
print(f"The year with the highest average temperature is {highest_year} with an average of {highest_avg:.2f}°C.")
