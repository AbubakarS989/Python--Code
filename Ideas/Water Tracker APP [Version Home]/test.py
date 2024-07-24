import os
import json

def ensure_json_file(file_path):
    """Ensure that the JSON file exists. If not, create it with an empty dictionary."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Creating a new one.")
        # Create an empty dictionary or list depending on your needs
        data = {}
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"File {file_path} created successfully.")
    else:
        print(f"File {file_path} already exists.")

# Example usage
if __name__ == "__main__":
    file_path = 'data.json'  # Specify your JSON file path here
    ensure_json_file(file_path)

    # Now you can proceed with loading and using the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("Data loaded from file:", data)
