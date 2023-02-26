import csv
import numpy as np
from PIL import Image

def create_image(csv_path,r,g,b):
    data = np.genfromtxt(csv_path, delimiter=',', skip_header=True)

    red_channel = data[:,r]
    green_channel = data[:,g]
    blue_channel = data[:,b]

    # Normalizing
    max_val = np.max([red_channel, green_channel, blue_channel])
    red_channel = (red_channel / max_val) * 255
    green_channel = (green_channel / max_val) * 255
    blue_channel = (blue_channel / max_val) * 255

    image_data = np.stack([red_channel, green_channel, blue_channel], axis=1)

    image_data = image_data.astype(np.uint8)
    image = Image.fromarray(image_data, mode='RGB')

    return image

#image= create_image(path,r,g,b)
#image.show()
