import os

def report_file_sizes(directory):
    try:
        # List all files and subdirectories in the given path
        contents = os.listdir(directory)
        print(f"File sizes in '{directory}':")
        for item in contents:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                file_size = os.path.getsize(item_path)
                print(f"{item}: {file_size} bytes")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")

# Call the function to report file sizes
report_file_sizes(directory_path)
