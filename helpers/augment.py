import imgaug as ia
import imgaug.augmenters as iaa
import os
from PIL import Image
import numpy as np

def augment_images_in_folder(folder_path, output_folder, augmenter, image_extension='.png'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the folder and apply augmentation
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extension):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            image_array = np.array(image)

            # Apply augmentation
            image_aug = augmenter(image=image_array)
            Image.fromarray(image_aug).save(os.path.join(output_folder, filename))

# Define your augmentations
seq = iaa.Sequential([
    iaa.Fliplr(0.5),  # horizontal flips
    iaa.Crop(percent=(0, 0.1)),  # random crops
    # Small gaussian blur with random sigma between 0 and 0.5.
    iaa.Sometimes(0.5, iaa.GaussianBlur(sigma=(0, 0.5))),
    # Strengthen or weaken the contrast in each image.
    iaa.ContrastNormalization((0.75, 1.5)),
    # Add Gaussian noise.
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    # Make some images brighter and some darker.
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    # Apply affine transformations to each image.
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8)
    )
], random_order=True)  # apply augmenters in random order

def process_all_subfolders(top_folder, output_base_folder):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        output_subfolder_path = os.path.join(output_base_folder, subfolder)
        # Check if it is a directory
        if os.path.isdir(subfolder_path):
            print(f"Augmenting images in folder: {subfolder_path}")
            augment_images_in_folder(subfolder_path, output_subfolder_path, seq)

# Example usage
top_folder = '/Users/anishpalakurthi/Desktop/FLAIR/flair_infarct_estimation/FLAIR_Images'  # Replace with your top-level folder path
output_base_folder = '/Users/anishpalakurthi/Desktop/FLAIR/flair_infarct_estimation/Augmented_FLAIR_Images'  # Replace with your desired output folder path
process_all_subfolders(top_folder, output_base_folder)
