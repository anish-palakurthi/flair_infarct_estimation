import cv2
import os

def apply_clahe(image_path, output_path, clip_limit=2.0, tile_grid_size=(8, 8)):
    img = cv2.imread(image_path, 0)  # Read the image in grayscale
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahed_img = clahe.apply(img)
    cv2.imwrite(output_path, clahed_img)

def process_images_in_folder(folder_path, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Apply CLAHE to each image in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            apply_clahe(image_path, output_path)

def process_all_subfolders(top_folder, output_base_folder):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        # Check if it is a directory
        if os.path.isdir(subfolder_path):
            output_folder = os.path.join(output_base_folder, subfolder)
            print(f"Processing folder: {subfolder_path}")
            process_images_in_folder(subfolder_path, output_folder)

# Example usage
top_folder = '/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels'  # Source folder path
output_base_folder = '/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels_CLAHE'  # Output folder path
process_all_subfolders(top_folder, output_base_folder)
