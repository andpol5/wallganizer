#!/usr/bin/env python3
#############################################
# Throw out walls not in: 1.33 <= aspect_ratio <= 1.8

import math
import os
import uuid
from pathlib import Path

import numpy as np
from skimage.io import imread, imsave
from skimage.transform import resize


WALL_DIR = 'walls'

MIN_RATIO = 1.33
MAX_RATIO = 1.80


def main():
    file_list = sorted(list(((Path(os.environ['HOME']) / 'Pictures') / WALL_DIR).glob('*')))
    np.random.shuffle(file_list)

    # Number of digits in the # of files (useful for enumeration with leading zeros)
    num_digits = int(math.ceil(math.log10(len(file_list))))

    for f in file_list:
        im = imread(f)

        aspect_ratio = im.shape[1] / im.shape[0]
        if aspect_ratio < MIN_RATIO or aspect_ratio > MAX_RATIO:
            print("deleting {} with ratio of {}".format(f, aspect_ratio))
        elif im.shape[1] > 2000:
            print("resizing {} with size of {} to 1920x1200".format(f, im.shape))
            im = resize(im, (1200, 1920))
            imsave(f, im)


if __name__ == '__main__':
    main()
