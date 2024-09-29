import cv2
import numpy as np
  
# enter image path
path='bottle_crate_01.png'
    
# Image read
img = cv2.imread(path, cv2.IMREAD_COLOR)
org_img=img.copy()    

# convert to grayscale image 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur using 3 * 3 kernel.
blur_img = cv2.blur(gray_img, (3, 3))

# Set parameter for hugh transformer & get bottles corrdinates
bottles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                                    param2 = 30, minRadius = 15, maxRadius = 25)

# No of bottles
count_bottles=0

# Draw circles on bottles
if bottles is not None:
    bottles = np.uint16(np.around(bottles))
    
    for bottle in bottles[0][:]:
        count_bottles+=1
        x, y, radius = bottle[0], bottle[1], bottle[2]

        # Draw circle on bottle top
        cv2.circle(img, (x, y), radius, (0, 255, 0), 2)

cv2.putText(img, 'Bottles : '+str(count_bottles), (10,30), cv2.FONT_HERSHEY_SIMPLEX,  1, (255, 0, 0), 2, cv2.LINE_AA)
print("Number of Bottles in Image :",count_bottles)

# Show original & detected bottles images together
cv2.imshow("Output",np.hstack([org_img,img]))
cv2.waitKey(0)