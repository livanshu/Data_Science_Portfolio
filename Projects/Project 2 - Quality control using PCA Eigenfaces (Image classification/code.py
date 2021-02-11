import numpy as np
import cv2
from matplotlib import pyplot as plt

image_width = 300
image_length = 300
total_pixels = image_width * image_length

images = 100
variants = 2
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

print(face_vector.shape)
print(face_vector)

avg_face_vector = face_vector.mean(axis=1)
avg_face_vector = avg_face_vector.reshape(face_vector.shape[0], 1)
normalized_face_vector = face_vector - avg_face_vector
print(avg_face_vector)
#print(normalized_face_vector)

covariance_matrix = np.cov(np.transpose(normalized_face_vector))
#print(covariance_matrix)

eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

#print(eigen_vectors.shape)
k = 20
k_eigen_vectors = eigen_vectors[0:k, :]
#print(k_eigen_vectors.shape)

eigen_faces = k_eigen_vectors.dot(np.transpose(normalized_face_vector))
#print(eigen_faces.shape)

weights = np.transpose(normalized_face_vector).dot(np.transpose(eigen_faces))
#print(weights)

test_img = cv2.imread("testing/" + "20" + ".jpeg")
test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2GRAY)

test_img = test_img.reshape(total_pixels, 1)
test_normalized_face_vector = test_img - avg_face_vector
test_weight = np.transpose(test_normalized_face_vector).dot(np.transpose(eigen_faces))

index = np.argmin(np.linalg.norm(test_weight - weights, axis=1))

if (index >= 0 and index < 100):
    print("The product is DEFECTIVE!")
if (index >= 100 and index < 200):
    print("The product is OKAY")

#print(covariance_matrix)
#print(eigen_faces.shape)
