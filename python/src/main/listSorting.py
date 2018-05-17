#!/usr/bin/python

#Begin import
import sys
import gc
import heapq
import string
#End import

#Heap Sort taken from Python Doc
#Begin heapsort
def heapsort(list):
	heap = []
	for value in list:
		heapq.heappush(heap, value)
	return [heapq.heappop(heap) for i in range(len(heap))]
#End heapsort

#Begin sanitize
def sanitize(list):
	validChar = '-'.join(string.ascii_letters).join(string.digits)
	sanitizeTable  = string.maketrans(validChar, ' ' * len(validChar))
	for i, value in enumerate(list):
		list[i] = value.translate(None, sanitizeTable)
	return list
#End sanitize

#Begin splitInputs
def splitInputs(list):
	num = []
	strings = []
	isNum = []
	for i, value in enumerate(list):
		try:
			sign = ''
			if value.startswith('-', 0, 1) :
				sign = '-'
			validChar = ''.join(string.digits)
			sanitizeTable  = string.maketrans(validChar, ' ' * len(validChar))
			num.append(int(sign+value.translate(None, sanitizeTable)))
			isNum.append(True)
		except ValueError:
			validChar = ''.join(string.ascii_letters)
			sanitizeTable  = string.maketrans(validChar, ' ' * len(validChar))
			orgValue = value.translate(None, sanitizeTable)
			strings.append((orgValue.lower(), orgValue))
			isNum.append(False)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	return(num, strings, isNum)
#End splitInputs

#Begin processInputs
def processInputs(inputFilePath):
	#Store input from file into buffer
	#Concern: Will test machine have enough memory for max constraint? 
	#Max constraint: 100,000 of 100 characters ASCII or int = roughly 100mb
	try:
		inputFile = open(inputFilePath, "r")
		inputRaw = inputFile.read()
		inputFile.close()
	except:
		print "Cannot open input file"
		exit()
	#Split raw input into string array
	inputs = inputRaw.split(' ')
	#clear memory
	del inputRaw
	#Remove all none alpha-num chars except -, needs - to id negative ints
	sanitize(inputs)
	#Split the input into a list of ints and strings
	num, strings, isNum = splitInputs(inputs)
	num = heapsort(num)
	strings = heapsort(strings)
	return constructOutput(num, strings, isNum)
#End processInputs

#Begin constructOutput
def constructOutput(num, strings, isNum):
	outputs = []
	for value in isNum :
		if value :
			outputs.append(str(heapq.heappop(num)))
		else :
			sortValue, orgValue = heapq.heappop(strings)
			outputs.append(str(orgValue))
	return outputs
#End constructOutput

#Write to the target output file
#Begin writeToOutputFile
def writeToOutputFile(outputFilePath, outputs):
	try:
		outputFile = open(outputFilePath, "w")
		length = len(outputs) - 1
		for i,value in enumerate(outputs) :
			if i == length:
				outputFile.write(value)
			else:
				outputFile.write(value + ' ')
		outputFile.close()
	except:
		print "Cannot open output file"
		exit()
#End writeToOutputFile
	
#Begin main
def main(argv):
	#Check for command lines arguments: needs input and output file
	if len(sys.argv) != 3 :
		sys.exit("Usage: ./listSorting.py path/to/input/file/input.txt path/to/output/file/result.txt")
	selfPath, inputFilePath, outputFilePath = sys.argv
	outputs = processInputs(inputFilePath)
	#Output to target file
	writeToOutputFile(outputFilePath, outputs)
	#Program completes
	exit()
#End main
	
#Define main
if __name__ == "__main__":
	main(sys.argv[1:])