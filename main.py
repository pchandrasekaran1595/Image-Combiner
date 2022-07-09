import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH  = os.path.join(BASE_PATH, "input")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

if not os.path.exists(OUTPUT_PATH): os.makedirs(OUTPUT_PATH)


def breaker(num: int = 50, char: str = "*") -> None:
    print("\n" + num*char + "\n")


def get_image(path: str) -> np.ndarray:
    return cv2.cvtColor(src=cv2.imread(path, cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)


def show_image(image, cmap: str = "gnuplot2") -> None:
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


def combine_images(image_1: np.ndarray, image_2: np.ndarray, vertical: bool, adapt_small: bool) -> np.ndarray:
    h1, w1, _ = image_1.shape
    h2, w2, _ = image_2.shape

    if vertical:
        if w1 > w2:
            if adapt_small:
                image_2 = cv2.resize(src=image_2, dsize=(w1, h2), interpolation=cv2.INTER_AREA)
            else:
                image_1 = cv2.resize(src=image_1, dsize=(w2, h1), interpolation=cv2.INTER_AREA)

        elif w2 > w1:
            if adapt_small:
                image_1 = cv2.resize(src=image_1, dsize=(w2, h1), interpolation=cv2.INTER_AREA)
            else:
                image_2 = cv2.resize(src=image_2, dsize=(w1, h2), interpolation=cv2.INTER_AREA)
                
        return np.vstack((image_1, image_2))
    
    else:
        if h1 > h2:
            if adapt_small:
                image_2 = cv2.resize(src=image_2, dsize=(w2, h1), interpolation=cv2.INTER_AREA)
            else:
                image_1 = cv2.resize(src=image_1, dsize=(w1, h2), interpolation=cv2.INTER_AREA)

        elif h2 > h1:
            if adapt_small:
                image_1 = cv2.resize(src=image_1, dsize=(w1, h2), interpolation=cv2.INTER_AREA)
            else:
                image_2 = cv2.resize(src=image_2, dsize=(w2, h1), interpolation=cv2.INTER_AREA)
                
        return np.hstack((image_1, image_2))


def main():
    args_1: tuple = ("--file1", "-f1")
    args_2: tuple = ("--file2", "-f2")
    args_3: tuple = ("--vertical", "-v")
    args_4: tuple = ("--adapt-big", "-ab")
    args_5: tuple = ("--save", "-s")

    filename_1: str = "Image_1.jpg" 
    filename_2: str = "Image_2.jpg"
    vertical: bool = False
    adapt_small: bool = True
    save: bool = False

    if args_1[0] in sys.argv: filename_1 = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename_1 = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: filename_2 = sys.argv[sys.argv.index(args_2[0]) + 1]
    if args_2[1] in sys.argv: filename_2 = sys.argv[sys.argv.index(args_2[1]) + 1]

    if args_3[0] in sys.argv or args_3[1] in sys.argv: vertical = True
    if args_4[0] in sys.argv or args_4[1] in sys.argv: adapt_small = False
    if args_5[0] in sys.argv or args_5[1] in sys.argv:  save = True

    assert filename_1 is not None, "Enter argument for --file1 | -f1"
    assert filename_2 is not None, "Enter argument for --file2 | -f2"

    assert filename_1 in os.listdir(INPUT_PATH), "File 1 Not Found"
    assert filename_2 in os.listdir(INPUT_PATH), "File 2 Not Found"

    image_1 = get_image(os.path.join(INPUT_PATH, filename_1))
    image_2 = get_image(os.path.join(INPUT_PATH, filename_2))

    image = combine_images(image_1, image_2, vertical, adapt_small)

    if save: cv2.imwrite(os.path.join(OUTPUT_PATH, "Combined.png"), cv2.cvtColor(src=image, code=cv2.COLOR_RGB2BGR))
    else: show_image(image)


if __name__ == "__main__":
    sys.exit(main() or 0)
