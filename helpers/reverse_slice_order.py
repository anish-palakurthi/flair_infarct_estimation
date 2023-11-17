import os

def reverse_file_naming(folder_path):
    # First, rename all files to a temporary unique name
    temp_rename_map = {filename: f"temp_{filename}" for filename in os.listdir(folder_path) if filename.endswith('.png')}
    for old_name, temp_name in temp_rename_map.items():
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, temp_name))

    # Determine the highest slice number
    max_slice_number = 0
    for temp_name in temp_rename_map.values():
        slice_number = int(temp_name.split('_slice_')[1].split('.png')[0])
        max_slice_number = max(max_slice_number, slice_number)

    # Rename files to their new names with reversed numbering starting at 0
    for temp_name in temp_rename_map.values():
        slice_number = int(temp_name.split('_slice_')[1].split('.png')[0])
        new_slice_number = max_slice_number - slice_number  # Adjusted line
        new_filename = temp_name.replace(f'_slice_{slice_number}', f'_slice_{new_slice_number}').replace('temp_', '')
        os.rename(os.path.join(folder_path, temp_name), os.path.join(folder_path, new_filename))
        print(f'Renamed {temp_name} to {new_filename}')

def process_all_subfolders(top_folder):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        # Check if it is a directory
        if os.path.isdir(subfolder_path):
            print(f"Processing folder: {subfolder_path}")
            reverse_file_naming(subfolder_path)

# Example usage
top_folder = '/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels/final_labels copy 2'  # Replace with your top-level folder path
process_all_subfolders(top_folder)

