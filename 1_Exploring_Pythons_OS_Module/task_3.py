import os

def count_file_extensions(directory):
    try:
        # Dictionary to store the count of each file extension
        extension_count = {}
        
        # List all files and subdirectories in the given path
        contents = os.listdir(directory)
        for item in contents:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                _, extension = os.path.splitext(item)
                if extension:
                    # Normalize the extension to lowercase and remove the leading dot
                    extension = extension[1:].lower()
                    if extension in extension_count:
                        extension_count[extension] += 1
                    else:
                        extension_count[extension] = 1
        
        print(f"File extension counts in '{directory}':")
        for ext, count in extension_count.items():
            print(f"{ext.upper()}: {count}")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")

# Call the function to count file extensions
count_file_extensions(directory_path)
