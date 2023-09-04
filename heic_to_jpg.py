
import os
import pyheif
from PIL import Image

def convert_heic_to_jpg(heic_file):
    with open(heic_file, "rb") as f:
        data = f.read()

    heic_image = pyheif.read_heif(data)
    jpg_image = Image.frombytes(heic_image.components[0].type, heic_image.size, heic_image.data)

    jpg_file = heic_file.replace(".heic", ".jpg")
    jpg_image.save(jpg_file)

    return jpg_file


def convert_heic_to_jpg_in_folder(folder_path):
    """Converts all HEIC images in a folder to JPG.

    Args:
      folder_path: The path to the folder containing the HEIC images.
    """

    for heic_file in os.listdir(folder_path):
        if heic_file.endswith(".heic"):
            jpg_file = convert_heic_to_jpg(os.path.join(folder_path, heic_file))
            print(f"HEIC image {heic_file} converted to JPG: {jpg_file}")


if __name__ == "__main__":
    folder_path = "/Users/manideep/Downloads/Data/Mouse Pics"
    convert_heic_to_jpg_in_folder(folder_path)

#%%
