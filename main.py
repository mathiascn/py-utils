from PIL import Image
import os

root_folder = 'C:/Users/mathi/code/py/imgresize/Devices'
scale = 0.47

def resize_images(root_folder, scale):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith(".PNG") or file_path.endswith(".png"):
                try:
                    with Image.open(file_path) as im:
                        size = tuple([int(scale * dim) for dim in im.size])
                        im_resized = im.resize(size, resample=Image.BILINEAR)
                        im_resized.save(file_path)
                        print(f"{file_path} was resized")
                except Exception as e:
                    print(f"Error resizing {file_path}: {e}")

resize_images(root_folder,scale)