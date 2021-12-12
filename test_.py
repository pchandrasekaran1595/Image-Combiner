import os
import numpy as np

from CLI.utils import handler


def test_combiner():
    image_1 = np.random.randint(low=0, high=255, size=(224, 224, 3)).astype("uint8")
    image_2 = np.random.randint(low=0, high=255, size=(360, 640, 3)).astype("uint8")

    assert handler.combine(image_1, image_2, False, True).shape == (360, 640+224, 3)

    image_1 = np.random.randint(low=0, high=255, size=(960, 1280, 3)).astype("uint8")
    image_2 = np.random.randint(low=0, high=255, size=(320, 480, 3)).astype("uint8")

    assert handler.combine(image_1, image_2, False, True).shape == (960, 1280+480, 3)

    image_1 = np.random.randint(low=0, high=255, size=(10, 20, 3)).astype("uint8")
    image_2 = np.random.randint(low=0, high=255, size=(10, 10, 3)).astype("uint8")

    assert handler.combine(image_1, image_2, False, True).shape == (10, 10+20, 3)


def test_full():
    args = ["", "-v", "--vertical", "--adpat-big", "-ab", "--save", "-s"]

    for arg in args:
        os.system("python main.py -f1 Image_1.jpg -f2 Image_2.jpg --wf " + arg)
