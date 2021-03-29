import os
from skimage import io
import numpy as np


def load_image(filename):
    if not os.path.isfile(filename):
        raise Exception('File not found.')

    img = io.imread(filename)
    return img


import matplotlib.pyplot as plt


def display_image(img_data):
    plt.imshow(img_data)


def load_all_images(directory, nimages=-1, ftype='.jpg'):
    if not os.path.isdir(directory):
        raise Exception('Directory not found.')

    # Collect all files ending with ftype
    filtered_files = []
    for file in os.listdir(directory):
        if file.endswith(ftype):
            filtered_files.append(file)

    # If nimages is larger than -1, we only load the first nimages files
    if nimages > -1:
        filtered_files = filtered_files[0:nimages]

    img_list = []
    for file in filtered_files:
        img = load_image(os.path.join(directory, file))
        img_list.append(img)

    return img_list

def draw_histogram(hist):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.bar(np.arange(len(hist)), hist)
    plt.xticks(np.arange(0, 10, len(hist)))
    plt.show()

