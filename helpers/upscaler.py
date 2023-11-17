from PIL import Image
import os

def upscale_images_in_folder(folder_path, output_folder, target_size=(512, 512)):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Open the image
                img_path = os.path.join(folder_path, filename)
                with Image.open(img_path) as img:
                    # Resize (upscale) the image
                    upscaled_img = img.resize(target_size)

                    # Save the upscaled image to the output folder
                    upscaled_img.save(os.path.join(output_folder, filename))
                    print(f"Upscaled and saved: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

def process_all_subfolders(top_folder, output_base_folder, target_size=(512, 512)):
    # Loop through each subfolder in the top folder
    for subfolder in os.listdir(top_folder):
        subfolder_path = os.path.join(top_folder, subfolder)
        # Check if it is a directory
        if os.path.isdir(subfolder_path):
            # Create a corresponding output directory for the subfolder
            output_dir = os.path.join(output_base_folder, subfolder)
            upscale_images_in_folder(subfolder_path, output_dir, target_size)

# Example usage
process_all_subfolders('/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels/AP_pngs', 
    '/Users/anishpalakurthi/Desktop/flair_infarct_estimation/FLAIR_Labels/upscaled_AP_pngs')


