import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((1000,1000,3), dtype='uint8')

def drawHex(dest, hex, radius):
    #center
	cv2.circle(dest, hex[:2], 7, (255,255,255*(hex[2]%2)), -1)
	points = np.zeros((6,2), dtype='int32')
	ang = 0
	for idx in range (0, 6):
		ang = np.deg2rad(idx * 60)
		x = (hex[0]+radius*np.sin(ang))
		y = (hex[1]+radius*np.cos(ang))
		cv2.circle(dest, (int(x),int(y)), 7, (0,255,0 ), -1)
		points[idx] = (int(x),int(y))

	points = points.reshape((-1,1,2))
	cv2.polylines(dest, [points], True, (255,0,0), 2)


def createHexList( center, radius, outers ):
	points = []
	points.append( (center[0], center[1], int(0)) )
	for outerIdx in range(1, outers+1):
		numHexes = outerIdx*6
		segment = 360 / numHexes
		
		if outerIdx%2 == 0:
			offset = 0
			r0 = (outerIdx+1)*radius
			r1 = 4*radius*np.sqrt(3)/2
		else:
			offset = segment/2
			r0 = 2*outerIdx*radius*np.sqrt(3)/2
			r1 = 2*outerIdx*radius*np.sqrt(3)/2

  
		for idx in range(0,numHexes):
			if idx%2==0:
				r = r0
			else:
				r = r1
			ang = np.deg2rad( segment*idx + offset )
			x = (center[0]+r*np.sin(ang))
			y = (center[1]+r*np.cos(ang))
			points.append( (int(x),int(y),outerIdx) )
	
	return points

R = 60
res = createHexList( (550,600), R, 3)
for hex in res:
	drawHex(img, hex, R )



plt.imshow(img)
plt.show()
