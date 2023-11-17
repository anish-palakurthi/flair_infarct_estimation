from PIL import Image
import os

def rotate_images_180(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.lower().endswith('.png'):
            try:
                # Open the image
                img_path = os.path.join(folder_path, filename)
                with Image.open(img_path) as img:
                    # Rotate the image 180 degrees
                    rotated_img = img.rotate(180)

                    # Save the rotated image
                    rotated_img.save(os.path.join(folder_path, filename))
                    print(f"Rotated and saved: {filename}")

            except Exception as e:
                print(f"Error rotating {filename}: {e}")

def process_all_subfolders(top_folder):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        # Check if it is a directory
        if os.path.isdir(subfolder_path):
            print(f"Processing folder: {subfolder_path}")
            rotate_images_180(subfolder_path)

# Example usage
process_all_subfolders('/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels/rotate_results')




