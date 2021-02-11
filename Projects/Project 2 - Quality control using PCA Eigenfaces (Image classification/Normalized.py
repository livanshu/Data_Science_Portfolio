import numpy as np
import cv2
from matplotlib import pyplot as plt

image_width = 300
image_length = 300
total_pixels = image_width * image_length

images = 2
variants = 1
total_images = images * variants

face_vector = []

for i in range(1, total_images + 1):
    x = cv2.imread("training_combined/" + str(i) + ".jpeg")
    face_image = cv2.cvtColor(x, cv2.COLOR_RGB2GRAY)
    #     plt.imshow(face_image, cmap = 'gray', interpolation = 'bicubic')
    #     plt.show()
    face_image = face_image.reshape(total_pixels, )
    face_vector.append(face_image)

face_vector = np.asarray(face_vector)
face_vector = face_vector.transpose()

#print(face_vector.shape)
print(face_vector)

avg_face_vector = face_vector.mean(axis=1)
avg_face_vector = avg_face_vector.reshape(face_vector.shape[0], 1)

print(avg_face_vector)
#print(avg_face_vector.shape)
normalized_face_vector = face_vector - avg_face_vector
#print(normalized_face_vector)

avg_face_reshape = np.reshape(normalized_face_vector,(300, 300))
import matplotlib.pyplot as plt
plt.imshow(avg_face_reshape, cmap="gray")
plt.savefig('Normalized_face_300x300.png')

#with open('facevector_75x75.csv', 'ab') as f:
 #   np.savetxt(f, face_vector, delimiter=",")

#covariance_matrix = np.cov((normalized_face_vector))
#print(covariance_matrix)

#with open('Covariance_matrix_75x75.csv', 'ab') as f:
#    np.savetxt(f, covariance_matrix, delimiter=",")

