import requests
import subprocess
import os

def download_file(url, save_path):
    """Download a file from a given URL and save it to the specified path."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {save_path}")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")

def run_file(file_path):
    """Execute the downloaded file using the command line."""
    try:
        # Depending on the file type, adjust the command to run
        if file_path.endswith('.exe'):
            subprocess.run([file_path], check=True)  # For .exe files
        else:
            subprocess.run(['cmd.exe', '/c', file_path], check=True)  # For other file types
        print(f"File executed successfully: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing file: {e}")

def main():
    # Define the URL and the local path to save the file
    url = "http://example.com/path/to/your/file.exe"  # Change this URL
    save_path = "downloaded_file.exe"  # Change this to the desired save path

    # Download the file
    download_file(url, save_path)

    # Run the downloaded file
    run_file(save_path)

if __name__ == "__main__":
    main()
