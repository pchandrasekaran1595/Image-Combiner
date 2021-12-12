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

    def save_image(self, image) -> None:
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
    
    def combine(self, image_1: np.ndarray, image_2: np.ndarray, orientation: str):
        pass


handler = Handler()

#######################################################################################################
