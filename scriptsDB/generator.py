import cv2

image = cv2.imread("../generated_images/generatedSamples_epoch39_batch50.png")
print(image.shape)
y = int(image.shape[0]/8)
x = int(image.shape[1]/8)
cropped = image[0:y, 0:x]
w = 280
h = 280
dim = (w, h)
resized = cv2.resize(cropped, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('scaled fox', resized)
cv2.waitKey(0)