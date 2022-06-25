from django.http import HttpResponse
from django.shortcuts import render, redirect
import joblib
from django.contrib import messages
# from .BC import blockchain, getBlockDetails, generateNextBlock

from tkinter import *

import PIL
from PIL import Image, ImageFont
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import *


def homepage(request):
    return render(request, "home.html")


def AddBlock(request):
    

    a=""
    temp = (request.GET["PID"])
    a+=temp[0]+temp[1]
    key=int(a)

    path = askopenfilename()

    print('The path of file : ', path)
   

    fin = open(path, 'rb')

    image = fin.read()
    fin.close()

    image = bytearray(image)

    for index, values in enumerate(image):
        # print(image[index])
        image[index] = values ^ key

    fin = open(path, 'wb')


    fin.write(image)
    fin.close()
    print('Encryption Done...')

    return redirect('/')


def result(request):

    a = ""
    # k=""
    temp = (request.GET["PIDD"])
    a += temp[0]+temp[1]
    key = int(a)
    path = askopenfilename()

    print('The path of file : ', path)
    print('Note : Encryption key and Decryption key must be same.')
    

    fin = open(path, 'rb')


    image = fin.read()
    fin.close()

    image = bytearray(image)

    for index, values in enumerate(image):
        # print(image[index])
        image[index] = values ^ key

    fin = open(path, 'wb')

    fin.write(image)
    fin.close()
    print('Decryption Done...')

    return render(request, "result.html")


#
