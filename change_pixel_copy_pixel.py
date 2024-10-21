import cv2
import random

def update_pixel(image_path):
    img = cv2.imread(image_path, -1)

    print(img.shape)

    # Change first 100 rows to random pixels
    for i in range(100):
	    for j in range(img.shape[1]):
		    img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    # Copy part of image
    tag = img[150:200, 90:130]
    img[50:100, 40:80] = tag

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Provide the path to the image file here
    image_path = 'assets/asset1.png'  # Replace with the path to your image file
    update_pixel(image_path)