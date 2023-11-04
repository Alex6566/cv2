import cv2
import pyautogui
from matplotlib import pyplot as plt
import os
import data_matrix
import numpy as np

z = os.listdir()
listName = []
listName = z
x = 0
for i in listName :
    x += 1

    img = cv2.imread(i)

    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()
    print(img.shape)
    height,width = img.shape[0:2]
    y = data_matrix.vec(img)
    print(f"image{x} : ",y, len(y))

for n in np.nditer(img):
    print(n,end="")

