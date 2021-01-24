import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image

rect = {"top": 160, "left": 160, "width": 400, "height": 400}

sct = mss()

while 1:
    screenshot = sct.grab(rect)
    img = Image.frombytes(
        "RGB", (screenshot.width, screenshot.height), bytes(screenshot.raw)
    )
    cv2.imshow("test", np.array(img))
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
