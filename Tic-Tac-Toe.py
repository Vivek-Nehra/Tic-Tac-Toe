import cv2
import numpy as np

def circle (x,y):
	cv2.circle(img,(x,y),80,(0,0,255),2)

def cross (x,y):
	cv2.line(img,(x-57,y-57),(x+57,y+57),(0,0,255),2)
	cv2.line(img,(x-57,y+57),(x+57,y-57),(0,0,255),2)

def position(value,x,y):
	if x<200 and x>0 and y<200 and y>0 :
		if value==1:
			circle(100,100)
		elif value==2:
			cross(100,100)
	elif x<400 and x>200 and y<200 and y>0 :
		if value==1:
			circle(300,100)
		elif value==2:
			cross(300,100)
	elif x<600 and x>400 and y<200 and y>0 :
		if value==1:
			circle(500,100)
		elif value==2:
			cross(500,100)
	elif x<200 and x>0 and y<400 and y>200 :
		if value==1:
			circle(100,300)
		elif value==2:
			cross(100,300)
	elif x<400 and x>200 and y<400 and y>200 :
		if value==1:
			circle(300,300)
		elif value==2:
			cross(300,300)
	elif x<600 and x>400 and y<400 and y>200 :
		if value==1:
			circle(500,300)
		elif value==2:
			cross(500,300)
	elif x<200 and x>0 and y<600 and y>400 :
		if value==1:
			circle(100,500)
		elif value==2:
			cross(100,500)
	elif x<400 and x>200 and y<600 and y>400 :
		if value==1:
			circle(300,500)
		elif value==2:
			cross(300,500)
	elif x<600 and x>400 and y<600 and y>400 :
		if value==1:
			circle(500,500)
		elif value==2:
			cross(500,500)
	global win
	win=checkwin()

def checkwin():
	count = 0
	for i in range(3):
		for j in range(3):
			if arr[i][j]!=0:
				count +=1
	if count==9:
		return 2 	#Draw
	elif (arr[0][0] == arr[0][1] and arr[0][1] == arr[0][2] and arr[0][0] != 0):
		cv2.line(img,(100,100),(500,100),(0,255,255),2)
		return 1
	elif (arr[1][0] == arr[1][1] and arr[1][1] == arr[1][2] and arr[1][0] != 0):
		cv2.line(img,(100,300),(500,300),(0,255,255),2)
		return 1
	elif (arr[2][0] == arr[2][1] and arr[2][1] == arr[2][2] and arr[2][0] != 0):
		cv2.line(img,(100,500),(500,500),(0,255,255),2)
		return 1
	elif (arr[0][0] == arr[1][0] and arr[1][0] == arr[2][0] and arr[0][0] != 0):
		cv2.line(img,(100,100),(100,500),(0,255,255),2)
		return 1
	elif (arr[0][1] == arr[1][1] and arr[1][1] == arr[2][1] and arr[0][1] != 0):
		cv2.line(img,(300,100),(300,500),(0,255,255),2)
		return 1
	elif (arr[0][2] == arr[1][2] and arr[1][2] == arr[2][2] and arr[0][2] != 0):
		cv2.line(img,(500,100),(500,500),(0,255,255),2)
		return 1
	elif (arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0] != 0):
		cv2.line(img,(100,100),(500,500),(0,255,255),2)
		return 1
	elif (arr[2][0] == arr[1][1] and arr[1][1] == arr[0][2] and arr[2][0] != 0):
		cv2.line(img,(100,500),(500,100),(0,255,255),2)
		return 1
	else:
		return 0


def callback(event,x,y,flag,call):
	if event==cv2.EVENT_LBUTTONDOWN:
		ycord =(int)(x/200)
		xcord =(int)(y/200)
		if arr[xcord][ycord]==0:
			global player
			player = player%2 +1
			arr[xcord][ycord] = player
			position(arr[xcord][ycord],x,y)
			
						
				
player = 0
arr=[[0,0,0],[0,0,0],[0,0,0]]
img = np.zeros([600,600,3],np.uint8)
cv2.namedWindow("Image")
cv2.setMouseCallback('Image',callback)
cv2.line(img,(200,0),(200,600),(0,255,0),2)
cv2.line(img,(400,0),(400,600),(0,255,0),2)
cv2.line(img,(0,200),(600,200),(0,255,0),2)
cv2.line(img,(0,400),(600,400),(0,255,0),2)
win=0
while 1:
	cv2.imshow("Image",img)
	if win==1:
		print "Congratulations! Player",player,"wins"
		break
	if win==2:
		print " Draw"
		break
	if cv2.waitKey(1)==ord('q'):
		break
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
