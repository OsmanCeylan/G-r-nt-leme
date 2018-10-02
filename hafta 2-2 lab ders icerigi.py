import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread("img.jpg")

def my_function_1(img_1):
    
    en_fazla = 0
    en_az = 0

    en_fazla = (img_1[:,:,0].max())
    en_az = (img_1[:,:,0].min())
    dimention = (img_1.ndim)
    shape=(img_1.shape)
    print("Dimention degeri =",dimention)
    print("Shape degeri = ",shape)
    print("En buyuk deger =",en_fazla)
    print("En kucuk deger =",en_az)
    print("En kucuk kirmizi renk degeri:",np.min(img_1[:,:,0]))
    print("En kucuk kirmizi renk degeri:",np.max(img_1[:,:,0]))
    print("En kucuk yesil renk degeri:",np.min(img_1[:,:,1]))
    print("En kucuk yesil renk degeri:",np.max(img_1[:,:,1]))
    print("En kucuk mavi renk degeri:",np.min(img_1[:,:,2]))
    print("En kucuk mavi renk degeri:",np.max(img_1[:,:,2]))
my_function_1(img_1)    