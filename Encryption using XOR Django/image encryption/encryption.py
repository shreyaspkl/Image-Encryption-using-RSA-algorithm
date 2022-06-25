# try block to handle exception
from tkinter.filedialog import askopenfilename

try:
	# take path of image as a input
	path = askopenfilename()

	# taking encryption key as input
	

	# print path of image file and encryption key that
	# we are using
	print('The path of file : ', path)
	print('Key for encryption : ', key)

	# open file for reading purpose
	fin = open(path, 'rb')

	# storing image data in variable "image"
	image = fin.read()
	fin.close()

	# converting image into byte array to
	# perform encryption easily on numeric data
	image = bytearray(image)

	# performing XOR operation on each value of bytearray
	for index, values in enumerate(image):
		image[index] = values ^ key

	# opening file for writing purpose
	fin = open(path, 'wb')

	# writing encrypted data in image
	fin.write(image)
	fin.close()
	print('Encryption Done...')


except Exception:
	print('Error caught : ', Exception.__name__)
