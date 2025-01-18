# ChatGPT's code

import os

def rename_files_in_folder():
    try:
        # Get the current folder where the script is located
        folder_path = os.getcwd()

        # Loop through each file in the folder
        for file_name in os.listdir(folder_path):
            # Check if 'exercise' is in the file name
            if 'exercise' in file_name:
                # Create the new file name by replacing 'exercise' with 'ex'
                new_file_name = file_name.replace('exercise', 'ex')

                # Get the full paths of the old and new file names
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, new_file_name)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{file_name}' -> '{new_file_name}'")

        print("File renaming completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the renaming function
rename_files_in_folder()
