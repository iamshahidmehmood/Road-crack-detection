#library imports here
import cv2
import math
import numpy as np
import scipy.ndimage

#create finction here
def orientated_non_max_suppression(mag, ang):
    ang_quant = np.round(ang / (np.pi/4)) % 4
    winE = np.array([[0, 0, 0],[1, 1, 1], [0, 0, 0]])
    winSE = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    winS = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
    winSW = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    magE = non_max_suppression(mag, winE)
    magSE = non_max_suppression(mag, winSE)
    magS = non_max_suppression(mag, winS)
    magSW = non_max_suppression(mag, winSW)

    mag[ang_quant == 0] = magE[ang_quant == 0]
    mag[ang_quant == 1] = magSE[ang_quant == 1]
    mag[ang_quant == 2] = magS[ang_quant == 2]
    mag[ang_quant == 3] = magSW[ang_quant == 3]
    return mag

def non_max_suppression(data, win):
    #create variable with data name for images
    data = scipy.ndimage.filters.maximum_filter(data, footprint=win, mode='constant')
    #condition if data == 0 return data

    #data[data != data] = 0

    data[data ==0]
    return data

# create here images read
gray_image = cv2.imread(r'C://Users//imuha//OneDrive//Desktop//savefile.jpg', 0)
'''
Non Maximum Suppression (NMS) is a technique used in many computer vision algorithms. 
It is a class of algorithms to select one entity (e.g. bounding boxes) out of many overlapping entities. 
The selection criteria can be chosen to arrive at particular results. Most commonly, 
the criteria is some form of probability number along with some form of overlap measure (e.g. IOU).
'''

#non-maximal-suppression = True
#with_nmsup = True
#applay and create  non-maximal suppression variable
nonmaximalsupppression = True

'''
 sigma basically controls how "fat" your kernel function is going to be; 
 higher sigma values blur over a wider radius. Since you're working with images,
 bigger sigma also forces you to use a larger kernel matrix to capture enough of the function's energy.
'''
fudgefactor = 1.3 #with this threshold you can play a little bit

'''
19

There's no formula to determine it for you; the optimal sigma will depend on image factors- primarily 
the resolution of the image and the size of your objects in it (in pixels).
'''
#for Gaussian Kernel
sigma = 21
#create kernal size here
kernel = 2 * math.ceil(2 * sigma) + 1

gray_image = gray_image/255.0
blur = cv2.GaussianBlur(gray_image, (kernel, kernel), sigma)
gray_image = cv2.subtract(gray_image, blur)

# compute sobel response
sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
mag = np.hypot(sobelx, sobely)
ang = np.arctan2(sobely, sobelx)

# threshold
threshold = 4 * fudgefactor * np.mean(mag)
mag[mag < threshold] = 0

#either get edges directly
#with_nmsup
if nonmaximalsupppression is False:
    mag = cv2.normalize(mag, 0, 255, cv2.NORM_MINMAX)
    kernel = np.ones((5,5),np.uint8)
    result = cv2.morphologyEx(mag, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('im', result)
    cv2.waitKey()

#or apply a non-maximal suppression
else:

    # non-maximal suppression
    mag = orientated_non_max_suppression(mag, ang)
    # create mask
    mag[mag > 0] = 255
    mag = mag.astype(np.uint8)

    kernel = np.ones((5,5),np.uint8)
    result = cv2.morphologyEx(mag, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('im', result)
    cv2.waitKey()
