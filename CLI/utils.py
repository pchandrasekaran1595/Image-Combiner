import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


READ_PATH = "Files"
SAVE_PATH = "Processed"


if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

#######################################################################################################

class Handler(object):
    def __init__(self) -> None:
        super().__init__()

    def read_image(self, path: str) -> np.ndarray:
        return cv2.imread(path, cv2.IMREAD_COLOR)

    def save_image(self, image: np.ndarray) -> None:
        cv2.imwrite(os.path.join(SAVE_PATH, "Processed.jpg"), image)

    def show(self, image: np.ndarray, title=None):
        plt.figure()
        plt.imshow(cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB))
        plt.axis("off")
        if title:
            plt.title(title)
        figmanager = plt.get_current_fig_manager()
        figmanager.window.state("zoomed")
        plt.show()
    
    def combine(self, image_1: np.ndarray, image_2: np.ndarray, vertical: bool, adapt_small: bool):
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


handler = Handler()

#######################################################################################################
