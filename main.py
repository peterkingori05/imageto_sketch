import cv2 as cv

# Reading the image
# Replace this image name with your image name
image = cv.imread("iron1.jpeg")

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not load image.")
    exit()

# Converting the Image into grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Inverting the Image
invert_image = cv.bitwise_not(gray_image)

# Blur the Image
blur_image = cv.GaussianBlur(invert_image, (21, 21), 0)

# Inverting the Blurred Image
invert_blur = cv.bitwise_not(blur_image)

# Convert Image Into sketch
sketch = cv.divide(gray_image, invert_blur, scale=256.0)

# Generating the Sketch Image named as Sketch.png
cv.imwrite("Sketch.png", sketch)

print("Sketch saved successfully as Sketch.png")
