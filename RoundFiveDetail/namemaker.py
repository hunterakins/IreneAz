import numpy as np 

'''
foldernames, letternames, numbers should all be lists of strings
basicpath gives the common oflder path of the the files, WHICH TERMINATES IN \\
extension is the extension as a string
NONE OF THESE INCLUDE \\
THE RETURNED OBJECT IS A LIST OF LISTS, ONE LIST FOR EACH FOLDER
WITHIN THE SUBLISTS ARE ALL THE FILENAMES IN THE FOLDER
SO filenames[i] will return a list of strings, each of which is the name and path of a file in the ith folder
'''


def makefilenames(foldernames, letternames, numbers, basicpath, extension):
	filenames = [0]*len(foldernames)
	for i in range(len(foldernames)):
		sublist = []
		for j in range(len(letternames)):
			for k in range(len(numbers)):
				item = basicpath+foldernames[i] + '/' + letternames[j] + numbers[k] + extension
				sublist.append(item)
		filenames[i] = sublist	
	return filenames



