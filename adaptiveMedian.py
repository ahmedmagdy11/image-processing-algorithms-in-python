import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

def imgConv(img, filt):
    out = np.multiply(img, filt)
    
    return out.sum()

def GetWindow (img , i , j , size):
    N = int (size / 2) 
    start_vert = i-N
    end_vert = i+N+1
    start_horiz = j-N
    end_horiz = j+N+1

    return img[start_vert:end_vert , start_horiz:end_horiz].reshape(size**2,)

def AdaptiveMean(img , Maxsize = 7):
    N =int(Maxsize/2) 
    Width = img.shape[0] - N 
    height = img.shape[0] - N 
    newimg = img.copy()
    for i in range(N , Width):
        for j in range(N , height):
            size = 3
            trueMedian = False
            while(size <= Maxsize):
                window = GetWindow(img , i , j , size)
                if (img[i,j] != window.max() and img[i,j] != window.min()):
                    trueMedian = True
                    break
                else : 
                    size = size + 2 
            if (trueMedian==False):
                newimg[i,j]= np.sort(window)[int((Maxsize**2 )/ 2)]
    return newimg

def Algorithm (ImagePath,maxwindowSize=7): 

    img = Image.open(ImagePath)
    img = np.asarray(img)
    newimg = img.copy()
    if (len(img.shape)== 3):
        
        newimg[:,:,0] = AdaptiveMean(img[:,:,0],maxwindowSize)
        newimg[:,:,1] = AdaptiveMean(img[:,:,1],maxwindowSize)
        newimg[:,:,2] = AdaptiveMean(img[:,:,2],maxwindowSize)
    else :
        newimg =AdaptiveMean(img,maxwindowSize)
    return newimg
# img = Algorithm('dog.jpg')
# plt.imshow(img)
# plt.show()


