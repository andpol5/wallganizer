#!/usr/bin/env python
#############################################
# Rename all walls to Width_Height_num_uuid.ext
import math
import os
import uuid
from pathlib import Path

import cv2
import numpy as np


WALL_DIR = 'walls'


def main():
    file_list = sorted(list(((Path(os.environ['HOME']) / 'Pictures') / WALL_DIR).glob('*')))
    np.random.shuffle(file_list)

    # Number of digits in the # of files (useful for enumeration with leading zeros)
    num_digits = int(math.ceil(math.log10(len(flist))))

    for i, f in enumerate(flist):
        im = cv2.imread(f)
        if im is None:
            continue

        newname = "{}x{}_{}_{}.{}".format(im.shape[0], im.shape[1],
                    str(i).zfill(num_digits), str(uuid.uuid4())[:8], f.suffix)
        print("{}/{} moving {} to {}".format(i + 1, len(file_list), f.name, newname))
        os.rename(f, f.parent / newname)


if __name__ == '__main__':
    main()
