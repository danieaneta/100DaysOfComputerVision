import cv2
import numpy as np

#Loading Image 
image = cv2.imread('Day-01/image.jpg')

"""
----------------------------------------------------------------
FLIPPING THE IMAGE: 
Within OpenCV, the cv2.flip() function is used to flip the image.
cv2.flip() takes two arguements: 
    1. The image you want to flip
    2. The axis you want to flip the image on.

The axis can be:
    0: Flip the image around the x-axis
    1: Flip the image around the y-axis
    -1: Flip the image around both axes

Below is an example of the flip function flipping the image on the x, y, and xy axis.
----------------------------------------------------------------
"""
flipped_y_axis = cv2.flip(image, 1)
flipped_x_axis = cv2.flip(image, 0)
flipped_xy_axis = cv2.flip(image, -1) 


"""
----------------------------------------------------------------
CROPPING AN IMAGE: 

Cropping an image is a bit more complex than flipping an image. 
If you've ever cropped an image on any image manipulation app, then you know it is a simple action. 
You can think of Adobe Photoshop, or GIMP cropping functionalities for example. 
The reason the cropping action is simple within software is because of the user interface. 
The foundation of the crop tool lies within the dimensions and coordinates within your image. 
In Computer Vision, you have to specify the dimensions and coordinates of the area you want to crop.

Try visualizing your image as a grid or split into invisible squares/quadrants.
Instead of drawing the section you want to crop with your mouse, you will state the x and y coordinates.

One thing important to remember is that the coordinate system in OpenCV starts at the top left of the image. 
When you specifty the x and y coordinates, the origin of the image is (0, 0) at the top left.
You could think about it like the -y quadrant in a graph.

----------------------------------------------------------------
"""

#USING THE .shape ATTRIBUTE, YOU CAN GET THE DIMENSIONS OF THE IMAGE
image_dimenstions = flipped_y_axis.shape
print(image_dimenstions)

x_start, y_start = 50, 50  # Top left corner
x_end, y_end = 200, 200    # Bottom right corner
cropped_image = flipped_y_axis[y_start:y_end, x_start:x_end]




# Step 4: Create a mask for bitwise operation
# Creating a black image of the same dimensions as the cropped image
mask = np.zeros(cropped_image.shape[:2], dtype="uint8")
# Adding a white rectangle to the mask
cv2.rectangle(mask, (25, 25), (175, 175), 255, -1)

# Step 5: Apply a bitwise AND operation using the mask
# This will only show the part of the image where the mask is white
bitwise_and_image = cv2.bitwise_and(cropped_image, cropped_image, mask=mask)

# Display the original, flipped, cropped, and bitwise AND images
cv2.imshow("Original Image", image)
cv2.imshow("Flipped Image", flipped_image)
cv2.imshow("Cropped Image", cropped_image)
cv2.imshow("Bitwise AND Image", bitwise_and_image)

# Wait for a key press and then close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()