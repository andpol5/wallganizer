#!/usr/bin/env python3
##############################################
# This script looks for duplicate walls and deletes them from the directory

import os
from pathlib import Path
from PIL import Image as PILImage

import imagehash
import numpy as np


WALL_DIR = 'walls'


def main():
    file_list = sorted(list(((Path(os.environ['HOME']) / 'Pictures') / WALL_DIR).glob('*')))

    # Create keys for every image hash.
    hash_dict = {}
    for i, f in enumerate(file_list):
        print("{}/{}".format(i + 1, len(file_list)))

        # Hash the image using a perceptual-hash https://www.phash.org/.
        im_hash = imagehash.phash(PILImage.open(f))
        hash_key = im_hash.hash.tobytes()

        if hash_key in hash_dict:
            print("duplicates \n 1: \"{}\"\n \"{}\"".format(hash_dict[hash_key], f))
            os.remove(f)
            continue
        else:
            hash_dict[hash_key] = f


if __name__ == '__main__':
    main()
