import collections
from operator import itemgetter

import numpy as np
from PIL import Image


wide = 25
tall = 6


def get_color_at(x: int, y: int, image: np.ndarray) -> int:
    for index, layer in enumerate(image):
        color = layer[y][x]

        if color != 2:
            return color


def print_image(img: np.ndarray):
    for line in img:
        for pixel in line:
            if pixel == 1:
                print('.', end='')
            elif pixel == 0:
                print('0', end='')
        print()


data = [int(char) for char in open('input', 'r').read()]

array = np.array(data).reshape(-1, 6, 25)
image = np.ones((6, 25))

for x in range(wide):
    for y in range(tall):
        image[y][x] = get_color_at(x, y, array)


print_image(image)

