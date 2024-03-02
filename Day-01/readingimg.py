import cv2 

"""
----------------------------------------------------------------------------
THIS IS HOW YOU READ AN IMAGE USING THE OPENCV LIBRARY:
----------------------------------------------------------------------------
"""
#The image is loaded as a NumPy array. In this case, it is stored within the variable 'img':
img = cv2.imread('Day-01/img.jpg')


"""
----------------------------------------------------------------------------
DISPLAYING THE IMAGE USING THE OPENCV LIBRARY:
----------------------------------------------------------------------------
"""
#Open the image within a window. We are naming the window 'Image', and inputing the argument 'img' which is the image we want to display: 
cv2.imshow('Image', img)
#Keep the image window open until keyboard key is pressed:
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
----------------------------------------------------------------------------
EXPLORING THE IMAGE DATA 
-It is important to understand the type of data you are working with when using the OpenCV library.
It will help you understand the type of operations you can perform on the data.
We will explore this further in another blog post when we talk about basic image processing.
----------------------------------------------------------------------------
"""

#Figuring out the data type of the image: 
print(img.dtype)
print(type(img))

