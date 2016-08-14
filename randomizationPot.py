#!/usr/bin/python 


#a[i][j] represents location of a given plant in the grid 
#0<=i<=3,0<=j<=3 

#generate 1 Million random float numbers between 0(in) and 1(ex)  using uniform distribution 
from numpy import random
listUniform= random.uniform(0,1,1000000)

#maps each plant to a coordinate in the grid for 100% light and 50% light group 
map100=[]
map50=[]

#fills the map100 and map50 using the random numbers generated using uniform distribution		
count = 0
while count != 16:
	valueOnGrid100= int((random.choice(listUniform)*33)%16)
	
	if valueOnGrid100 not in map100:
		map100.append(valueOnGrid100)
		count= count + 1

count=0
while count != 16:
	valueOnGrid50= int((random.choice(listUniform)*33)%16)
	
	if valueOnGrid50 not in map50:
		map50.append(valueOnGrid50)
		count= count + 1



#converts a given coordinate into an index 
def tupleToIndex(coordinate):
	arrayToGrid={0:(0,0),1:(0,1),2:(0,2),3:(0,3),4:(1,0),5:(1,1),6:(1,2),7:(1,3),8:(2,0),9:(2,1),10:(2,2),11:(2,3),12:(3,0),13:(3,1),14:(3,2),15:(3,3)}
	for key, value in arrayToGrid.iteritems():
		if value[0]==coordinate[0] and value[1]==coordinate[1]:
			return key

#converts an index to a tupple(coordinate)
def indexToTuple(index):
	arrayToGrid={0:(0,0),1:(0,1),2:(0,2),3:(0,3),4:(1,0),5:(1,1),6:(1,2),7:(1,3),8:(2,0),9:(2,1),10:(2,2),11:(2,3),12:(3,0),13:(3,1),14:(3,2),15:(3,3)}
	for key, value in arrayToGrid.iteritems():
		if index==key:
			return arrayToGrid[key]

#converts a given index(location on the grid) to a text for plants under 100% light 
def indexToText100(index):
	arrayToText100={0:'100-Control-1',1:'100-Control-2',2:'100-Control-3',3:'100-Control-4',4:'100-N(0.01)-1',5:'100-N(0.01)-2',6:'100-N(0.01)-3',7:'100-N(0.01)-4',8:'100-N(0.05)-1',9:'100-N(0.05)-2',10:'100-N(0.05)-3',11:'100-N(0.05)-4',12:'100-N(0.10)-1',13:'100-N(0.10)-2',14:'100-N(0.10)-3',15:'100-N(0.10)-4'}
	for key, value in arrayToText100.iteritems():
		if key==index:
			return arrayToText100[key]

#converts a given index(location on the grid) to a text for plants under 50% light 
def indexToText50(index): 
	arrayToText50={0:'50-Control-1',1:'50-Control-2',2:'50-Control-3',3:'50-Control-4',4:'50-N(0.01)-1',5:'50-N(0.01)-2',6:'50-N(0.01)-3',7:'50-N(0.01)-4',8:'50-N(0.05)-1',9:'50-N(0.05)-2',10:'50-N(0.05)-3',11:'50-N(0.05)-4',12:'50-N(0.10)-1',13:'50-N(0.10)-2',14:'50-N(0.10)-3',15:'50-N(0.10)-4'}
	for key, value in arrayToText50.iteritems():
		if key==index:
			return arrayToText50[key] 


#use of GUI framework to generate grid on the screen for plants under 100% and 50% light 
from Tkinter import *
master =Tk()
left=Frame(master)
left.pack(side=LEFT,expand=True, fill=Y)


right=Frame(master)
right.pack(expand=True, fill=BOTH) 
wLeft=[[0 for j in range(4)] for i in range(4)]
wRight=[[0 for j in range(4)] for i in range(4)]


for i in range(4):
	for j in range(4):
		
		wLeft[i][j]= Text(left, bg='#FFFF00', height=8, width=15, bd=5)
		wRight[i][j]= Text(right,bg='#F0E68C', height=8, width=15,bd=5)
		wLeft[i][j].grid(row=i, column=j)
		wRight[i][j].grid(row=i, column=j)
		
for i in range(4):
	for j in range(4):
		
		currentIndex=tupleToIndex((i,j))
		plantText100=indexToText100(currentIndex)
		plantText50=indexToText50(currentIndex)
		plantMoveToIndex100=map100[currentIndex]
		plantMoveToIndex50=map50[currentIndex]

		plantMoveToTupple100=indexToTuple(plantMoveToIndex100)
		plantMoveToTupple50=indexToTuple(plantMoveToIndex50)
		x100,y100=plantMoveToTupple100
		x50,y50=plantMoveToTupple50


		wLeft[x100][y100].insert(INSERT,plantText100, 'big')
		wRight[x50][y50].insert(INSERT,plantText50, 'big')



master.wait_window()


