# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:51:18 2020

@author: pedro

Chromakey
"""


import cv2

imgDir = '../imageDatabase/'
imgPath = imgDir+'falcon.jpg'
maskPath = imgDir+'mask.png'
backgroundPath = imgDir+'florest.jpg'


img = cv2.imread(imgPath)
mask = cv2.imread(maskPath)
background = cv2.imread(backgroundPath)


newImg = img

def apply_mask():
    
    
    falcon = cv2.bitwise_and(img,mask)
    back = cv2.bitwise_and(background,cv2.bitwise_not(mask))
    newImg =  falcon + back


    cv2.imshow('falcon' , falcon)
    cv2.imshow('back' , back)
    cv2.imshow('Chroma key img', newImg)
    
    cv2.imwrite(imgDir + 'processedImg/bitwise_mask.png' , newImg)


def mask2():
    global newImg
    falcon = cv2.multiply(img, mask, scale=1.0/255)
    back = cv2.multiply(background, 255 - mask, scale=1.0/255)
    newImg = cv2.add(falcon, back)
    
    
    cv2.imshow('falcon',falcon)
    cv2.imshow('back' , back)
    cv2.imshow('chroma key 2' , newImg)

    cv2.imwrite(imgDir + 'processedImg/scalar_mask.png' , newImg)


def blurring():
    cv2.imshow('originalImg',newImg)

    blurImg = cv2.blur(newImg, (10,10))
    cv2.imshow('blurred Img' , blurImg)
    
    medianBlur = cv2.medianBlur(newImg, 9) # perguntar porque valor de k % 2 tem de ser 1
    cv2.imshow('medianBlur' , medianBlur)
    
    gausianBlur = cv2.GaussianBlur(newImg, (5,5), 0)
    cv2.imshow('gausianBlur' , gausianBlur)


def trans_geo():
    img = newImg
    print('show')
    rot_mat = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2),30,1)
    print('mat')    
    rot_dst = cv2.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]))
    print('rot')
    cv2.imshow('Source image', img)
    cv2.imshow('Rotate', rot_dst)
    
    
try:
    apply_mask()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    mask2()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    trans_geo()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
except Exception as e:
    print(e)
    cv2.destroyAllWindows()