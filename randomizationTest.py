#!/usr/bin/python 
#implementation of randomization test 

#import itertools package to generate permutation exhaustively 

'''
#this section will include codes for user input of the two lists
#this will concatenate the lists to give a single lists
#stores the size of each list of numbers
#the concatenated list will be stored in variable called listNum
#sizeList1, sizeList2 will store the size of the individual list
'''
from sortedcontainers import SortedDict
import matplotlib.pyplot as plt 
#this is test data 
list1= [21,34,354,52,23]
list2=[12,53,64,81]
listNum=list1+ list2
sizeList1=len(list1)
sizeList2=len(list2)



#returns a list which includes all the permutations
#each individual permutation is stored as a tuple [(), (), ()]


#takes in size of the list as an argument and returns the total number of permutations 
def calculateTotalPermutations(sizeList):
	if sizeList==1:
		return 1
	return sizeList * calculateTotalPermutations(sizeList-1) 


def meanClass(listNum, sizeList1, sizeList2):
	#package to generate exhaustive permuations
	import itertools 
	
	permutations = list(itertools.permutations(listNum))

	#python dictionary that stores difference in mean as a key and the count as value
	meanClass={}
	
	for tuple in permutations:
				
		meanList1=sum(tuple[0:sizeList1])/sizeList1 
		meanList2=sum(tuple[sizeList1:])/sizeList2
		meanDifference= meanList1-meanList2
		if not meanClass.has_key(meanDifference):
			meanClass[meanDifference]= 1
		else:
			meanClass[meanDifference]= meanClass[meanDifference]+ 1 
		
	return meanClass 

unsortedMeanClass= meanClass(listNum, sizeList1, sizeList2)

sortedMeanClass= SortedDict(unsortedMeanClass)
tupleList= sortedMeanClass.items()
plotCoordinates= zip(*tupleList)
#print plotCoordinates
x= list(plotCoordinates[0])
y=list(plotCoordinates[1])

plt.plot(x,y,'ro')
plt.show()

'''
sum=0

for tuple in sortedMeanClass.items():
	sum=sum+ tuple[1]
	
print sum

print calculateTotalPermutations(9)
'''