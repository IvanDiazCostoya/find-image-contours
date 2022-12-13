import cv2

# Create window with freedom of dimensions
cv2.namedWindow("output", cv2.WINDOW_NORMAL)

# Read image (BGR). im es un <class 'numpy.array'>
im = cv2.imread("image.jpg")

median = cv2.medianBlur(im, 1)

imgray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,255,0), 3)

print('Total de contours: ', len(contours))

# Show image
cv2.imshow("output", im)

cv2.imwrite('contours.jpg', im)

cv2.waitKey()
