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
        new_filename = f'slice_{i}.png'
        img.save(os.path.join(output_dir, new_filename))

# Example usage for a single .nii file
nii_path = '/Users/anishpalakurthi/Desktop/FLAIR/flair_infarct_estimation/A_5435846_MR/10776201_8_threshold1.nii'  # Replace with the path to your .nii file
output_dir = '/Users/anishpalakurthi/Desktop/FLAIR/flair_infarct_estimation/nii_test_dir'  # Replace with your desired output directory path
convert_nii_to_images(nii_path, output_dir)
