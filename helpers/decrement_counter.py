import os

def decrement_file_numbering(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            parts = filename.split('_slice_')
            if len(parts) == 2:
                # Extract the slice number and the file extension
                slice_number, extension = parts[1].split('.', 1)
                new_slice_number = int(slice_number) - 1  # Decrement the number

                # Construct the new filename
                new_filename = f'{parts[0]}_slice_{new_slice_number}.{extension}'
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                print(f"Renamed {filename} to {new_filename}")

def process_all_subfolders(top_folder):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        # Check if it is a directory
        if os.path.isdir(subfolder_path):
            print(f"Processing folder: {subfolder_path}")
            decrement_file_numbering(subfolder_path)

# Example usage
top_folder = '/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels/final_labels'  # Replace with your top-level folder path
process_all_subfolders(top_folder)
