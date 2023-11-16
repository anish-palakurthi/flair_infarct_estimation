import pydicom
from PIL import Image
import numpy as np
import os

def convert_dcm_to_images(dcm_folder, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each DICOM file in the folder
    for filename in os.listdir(dcm_folder):
        if filename.endswith('.dcm'):
            try:
                # Read DICOM file
                dcm_path = os.path.join(dcm_folder, filename)
                dcm_data = pydicom.read_file(dcm_path)
                image_array = dcm_data.pixel_array

                # Normalize the image array
                image_array = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))

                # Convert to PIL image and save
                img = Image.fromarray(np.uint8(image_array * 255))
                new_filename = f'{os.path.basename(dcm_folder)}_{filename.replace(".dcm", ".png")}'
                img.save(os.path.join(output_dir, new_filename))

            except Exception as e:
                print(f"Error processing {filename} in {dcm_folder}: {e}")

def process_all_subfolders(top_folder, output_base_dir):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        if os.path.isdir(subfolder_path):
            output_dir = os.path.join(output_base_dir, subfolder)
            convert_dcm_to_images(subfolder_path, output_dir)

# Example usage
process_all_subfolders('/Users/anishpalakurthi/Desktop/FLAIR/FLAIR_Images/AP_images',
                       '/Users/anishpalakurthi/Desktop/FLAIR/FLAIR_Images/png_AP_output')
