import cv2
import numpy as np
import matplotlib.pyplot as plt

def getTextOverlay(input_image):
    # output = np.zeros(input_image.shape, dtype=np.uint8)
     
    # Write your code here for output
    image_copy = np.copy(input_image)
    image_copy = cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)
    # image_copy = np.copy(input_image)
    # ret, mask = cv2.threshold(input_image,100,250,cv2.THRESH_BINARY)
    # mask_inv = cv2.bitwise_not(mask)
    l_black = np.array([0,0,0])
    u_black = np.array([15,15,15])
    
    mask = cv2.inRange(image_copy, l_black, u_black)
    # mask_copy = np.copy(mask)
    # output = cv2.cvtColor(mask_copy ,cv2.COLOR_BGR2GRAY)
    # plt.imshow(mask)
    # plt.show()
    output = cv2.bitwise_not(mask)
    # plt.imshow(output, cmap='gray')
    # plt.show()
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    # output = cv2.resize(output, (720,480))
    cv2.imwrite('simpons_text.png', output)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()