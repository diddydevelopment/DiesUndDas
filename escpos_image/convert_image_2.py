from PIL import Image,ImageFilter,ImageOps
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.ndimage.filters import convolve

def createBinaryImage(imgpath,width,height):
	imgpil = Image.open(imgpath)
	imgpil = ImageOps.autocontrast(imgpil,cutoff=20)
	imgpil = imgpil.resize((width,height), Image.ANTIALIAS)
	img = np.array(imgpil,np.float32)
	r = 0.2989 * img[:,:,0]
	g = 0.5870 * img[:,:,1]
	b = 0.1140 * img[:,:,2]
	imgbw = np.add(r,np.add(g,b))
	imgbw = imgbw / 255
	imgbw = 1-imgbw

	#imgbw  = imgbw - 0.5
	#imgbw = imgbw * 1.3
	#imgbw  = imgbw + 0.5
	#imgbw[imgbw > 1] = 1
	#imgbw[imgbw < 0] = 0

	#print(np.mean(imgbw))
	#print(np.min(imgbw))
	#print(np.max(imgbw))
	
	#edges = imgpil.filter(ImageFilter.Kernel((5,5), [0,2,5,2,0,0,2,5,2,0,0,2,5,2,0,0,2,5,2,0,0,2,5,2,0], scale=None, offset=0))
	#kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
	#kernel = np.true_divide(kernel,np.sum(kernel))
	#edges = convolve(imgbw,kernel)

	#edges = edges - np.min(edges)
	#edges = np.true_divide(edges,np.max(edges))
	#print(np.mean(edges))
	#print(np.min(edges))
	#print(np.max(edges))

	#plt.imshow(edges,cmap='Greys',  interpolation='nearest')
	#plt.show()

	##my method of creating a binary image
	if(False):
		imgbin = np.zeros((height,width),np.int8)

		choose_random = 0.05
		threshold = 0.8
		for i,pi in enumerate(imgbw):
			for j,pj in enumerate(pi):
				randomvote = 1 if random.random() < imgbw[i,j] else 0
				if random.random() < choose_random:
					imgbin[i,j] = randomvote
				else:
					imgbin[i,j] = 1 if imgbw[i,j] > threshold else 0
	else:

		imgbw = imgbw * 255
		imgbw = np.array(imgbw,np.uint8)
		imgbw_pil = Image.fromarray(imgbw,'L')

		imgbw1 = imgbw_pil.convert('1').convert('L')
		imgbin = np.array(imgbw1,np.bool)
	return imgbin

def getESCPOSCode(img,width,height,batch_height=1):

	ints = np.array([128,64,32,16,8,4,2,1])
	escpos_len = (width*height)/8
	escpos = np.zeros(escpos_len,np.uint8)
	escpos_i = 0
	for i in range(0,height,batch_height*8):
		for j in range(width):
			for iter in range(0,8*batch_height,8):
				b = img[i+iter:i+iter+8,j]
				bval = np.sum(ints[np.where(b)[0]])
				escpos[escpos_i] = bval
				escpos_i = escpos_i +1

	##for use with e.g. arduino
	#vals = ','.join(str(es) for es in escpos)
	#print('const int escpos_len = '+str(int(escpos_len))+';')
	#print('const byte escpos[escpos_len] = {'+vals+'};')
	#print('const int width = '+str(width)+';')
	#print('const int height = '+str(height)+';')
	#print('const int batch_height = '+str(batch_height)+';')
	return escpos

if __name__ == '__main__':
	imgbin = createBinaryImage('portrait.jpg',96,96)

	escpos = getESCPOSCode(imgbin,96,96)

	print(escpos)

	plt.imshow(imgbin,cmap='Greys',  interpolation='nearest')
	plt.show()
