# import math
import cv2
# import matplotlib.pyplot as plt

# *********************************
# * funstions irrelative to steps *
# *********************************

def imshow(image, title='', isend=True):
    cv2.imshow(title, image)
    if isend:
        k = cv2.waitKey(0)
        if k:
            cv2.destroyAllWindows()
