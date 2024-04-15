import cv2
import numpy as np 

image = cv2.imread('Day-03/01.jpg')

image = cv2.resize(image, (500, 500))
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
----------------------------------------------------------------
CONVERTING THE IMAGE TO HSV: 

Why? 

HSV is more robust and easier to use when you need to detect specific colors regardless of lighting variations.
BGR colors are represented through combinations of red, green, and blue components. 
These components are highly sensitive to lighting variations. This can alter the perceived color. 
----------------------------------------------------------------
"""

#Converting the image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

"""
----------------------------------------------------------------
LOWER AND UPPER BOUNDARIES FOR THE COLOR: 

Explanation: 

lower_green = 
    [50, 100, 100]
    hue, saturation, and value respectively.

upper_green = 
    [70, 255, 255]
    hue, saturation, and value respectively.

Within OpenCV, Hue values are between 0 and 180 to maintain an 8-bit format. 
 -Normally, Hue values are between 0 and 360 representing the color wheel.
    -Red[0-10]
    -Orange[10-20]
    -Yellow[20-30]
    -Green[50-70]
    -Cyan[85-95]
    -Blue[110-130]
    -Violet[130-145]
    -Magenta[145-160]

Saturation values are between 0 and 255.

Saturation[0] = No color present in the pixel, it is completely gray. 
    - Low saturations appear more washed out. 

Saturation[255] = The color is completely saturated. Represents the fullest color intensity, 
with no white mixed in. 
    - Colors with high saturation will appear more vibrant.

Value values are between 0 and 255.
    - Value[0] = Black. Represents complete darkness, regardless of hue and satursation levels. 
    - Value[255] = Brightest intensity of the specified color. 
----------------------------------------------------------------
"""


lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

mask = cv2.inRange(hsv_image, lower_green, upper_green)

segmented_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Day-03/segmented_image.jpg', segmented_image)
cv2.imwrite('Day-03/mask.jpg', mask)
cv2.imwrite('Day-03/hsv_image.jpg', hsv_image)
cv2.imwrite('Day-03/01.jpg', image)
