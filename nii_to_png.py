import nibabel as nib
from PIL import Image
import numpy as np
import os

def convert_nii_to_images(nii_path, output_dir, is_mask=False):
    # Load NII file
    nii_file = nib.load(nii_path)
    data = nii_file.get_fdata()

    # Normalize the image array if it's not a mask
    if not is_mask:
        data = (data - np.min(data)) / (np.max(data) - np.min(data))

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each slice in the NII file
    for i in range(data.shape[2]):
        # Extract the slice
        slice_2d = data[:, :, i]

        # Convert to PIL image and save
        img = Image.fromarray(np.uint8(slice_2d * 255))
        # Constructing a new filename
        new_filename = f'{os.path.splitext(os.path.basename(nii_path))[0]}_slice_{i}.png'
        img.save(os.path.join(output_dir, new_filename))

def process_all_nii_files(folder_path, output_base_dir, is_mask=False):
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.nii'):
            file_path = os.path.join(folder_path, filename)
            # Create a corresponding output directory for the NII file
            output_dir = os.path.join(output_base_dir, os.path.splitext(filename)[0])
            convert_nii_to_images(file_path, output_dir, is_mask)

# Example usage for images
process_all_nii_files('/Users/anishpalakurthi/Desktop/FLAIR/FLAIR_Images/KESHAV_images', '/Users/anishpalakurthi/Desktop/FLAIR/FLAIR_Images/png_KESHAV_output')

# Example usage for masks
# process_all_nii_files('/path/to/nii/mask_folder', '/path/to/output/masks_folder', is_mask=True)
