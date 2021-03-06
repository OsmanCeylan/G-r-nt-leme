from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# sorunun a ��kk�n�n cevab�
def matris_create_28_by_28_with_0_1(): #28x28 boyutunda, i�eri�i 0 ve 1 olan birim matris olusturan fonksiyon
    my_matris = np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            my_matris[i,j] = random.randint(0,2)
    return my_matris


# sorunun b ��kk�n�n cevab�
def MBR_create_28_by_28_with_0_1(matris_a):  #a ��kk�nda �retilen matriste 1leri i�eren MBR dikd�rtgenini �reten fonksiyonu yaz�n�z
    m = matris_a.shape[0]
    n = matris_a.shape[1]
    x_min = m #baslangic degerleri olas� en olumsuz durum 
    x_max = 0
    y_min = n
    y_max = 0
    for i in range(m):
        for j in range(n):
            if (matris_a[i,j] == 1 and x_min > i):  # resim/matris uzerinden 
                x_min = i                          # x_min, ... guncelleniyor
            if (matris_a[i,j] == 1 and x_max < i):
                x_max = i
            if (matris_a[i,j] == 1 and y_min > j):
                y_min = j
            if (matris_a[i,j] == 1 and y_max < j):
                y_max = j
    return (x_min, x_max, y_min, y_max)    




# c ��kk�n�n cevab�
def get_similarity(character_a,character_b): # iki matrisin(vekt�r�n) benzerli�ini return eden fonksiyon
    m = character_a.shape[0]
    n = character_a.shape[1] 
    my_similarity = 0
    for i in range(m):
        for j in range(n):
            my_similarity = my_similarity + character_a[i,j]*character_b[i,j]
    return my_similarity


m_10 = matris_create_28_by_28_with_0_1()
get_similarity(m_10,m_10)



## d ��kk�n�n cevab�
def get_similarity_for_many_matrix(kac_karakter):
    kac_karakter = 100
    D = matris_create_28_by_28_with_0_1()
    liste = []
    for i in range(kac_karakter):
        D = matris_create_28_by_28_with_0_1()
        liste.append(D)
    for j in liste:
        simila = get_similarity(liste[0],j)
        print(simila)



A = matris_create_28_by_28_with_0_1()
B = matris_create_28_by_28_with_0_1()

C = MBR_create_28_by_28_with_0_1(A)



D = get_similarity(A,B)


get_similarity_for_many_matrix(A)
