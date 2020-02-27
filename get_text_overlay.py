import cv2
import numpy as np
import matplotlib.pyplot as plt

def getTextOverlay(input_image):
     
    # Write your code here for output
    image_copy = np.copy(input_image)
    image_copy = cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)
    l_black = np.array([0,0,0])
    u_black = np.array([15,15,15])
    
    mask = cv2.inRange(image_copy, l_black, u_black)
    output = cv2.bitwise_not(mask)
    # plt.imshow(output, cmap='gray')
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
    # cv2.imshow('simpons_text.png', output)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
