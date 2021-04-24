# Road-crack-detection
 Python 
#library imports here
import cv2
import math
import numpy as np
import scipy.ndimage

Remove the inhomogeneous background illumination.
A big gaussian blurring and subtract the original image from the blurred one.
Sobel edge detection and a morphological close.
Remove the noise using blob analysis (e.g. remove regions with small areas).
In principle, you have to convert the image between 0 and 1 before GaussianBlur. Additionally to get better results you also can apply a non-maximal suppression after Sobel.

![detect-img](https://user-images.githubusercontent.com/82101704/115952588-36a07300-a500-11eb-88fc-289e524c81aa.png)
![real-img](https://user-images.githubusercontent.com/82101704/115952589-386a3680-a500-11eb-8351-3efac78688dd.PNG)
![real-img1](https://user-images.githubusercontent.com/82101704/115952590-3a33fa00-a500-11eb-9f7c-dd9da1031873.png)
![detect-img1](https://user-images.githubusercontent.com/82101704/115952592-3b652700-a500-11eb-9a17-a40217004f01.PNG)


