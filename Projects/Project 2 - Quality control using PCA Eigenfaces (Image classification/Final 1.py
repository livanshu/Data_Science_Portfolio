import numpy as np
import cv2
import os

IMG_DIR = 'F:\McMaster\Multivariate\Casting Project\Casting_data\Train\Ok_front'

for img in os.listdir(IMG_DIR):
        img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)

        img_array = (img_array.flatten())

        img_array  = img_array.reshape(-1, 1).T

        print(img_array)

        with open('Train_Ok_final.csv', 'ab') as f:

            np.savetxt(f, img_array, delimiter=",")