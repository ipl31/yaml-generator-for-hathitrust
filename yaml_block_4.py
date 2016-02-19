# Goal: Print list of images in proper YAML format.
# Goal: Handle reading order.

def determinePrefixLength(pageNum):
	global prefixZeroes
	if 0 < pageNum < 10:
		prefixZeroes = '0000000'
	elif 10 <= pageNum < 100:
		prefixZeroes = '000000'
	elif 100 <= pageNum < 1000:
		prefixZeroes = '00000'
	elif 1000 <= pageNum < 10000:
		prefixZeroes = '0000'
	else:
		prefixZeroes = 'error'
		
def generateFileName(prefix, suffix, fileType):
	global fileName
	fileName = prefix + str(suffix) + '.' + fileType

def generateOrderLabel(readingStartNum, pageNum, orderNum):
	global orderLabel
	orderLabel = ''
	if pageNum >= readingStartNum:
		orderLabel = 'orderlabel: "' + str(orderNum) + '"'

def generateLabel(pageNum, frontCover):
	global label
	label=''
	if pageNum == frontCover:
		label='label: "FRONT_COVER"'

def writeFile(finalNumber, readingStartNum, fileType, outputFile):
	f = open(outputFile, 'w')
	pageNum = 1
	orderNum = 1
	while pageNum <= finalNumber:
		determinePrefixLength(pageNum)
		generateFileName(prefixZeroes, pageNum, fileType)
		generateOrderLabel(readingStartNum, pageNum, orderNum)
		generateLabel(pageNum, frontCover)
		comma = ''
		if orderLabel != '' and label !='':
			comma = ', '
		output = '\t' + fileName + ': { ' + orderLabel + comma + label + ' }\n'
		f.write(output)
		if pageNum >= readingStartNum:
			orderNum += 1
		pageNum += 1
	f.close()

fileType = raw_input("What is the (lowercase) filetype? ")

finalNumber = int(raw_input("What is the number of the final image? "))

readingStartNum = int(raw_input("What is the file number on which page 1 occurs? "))

frontCover = int(raw_input("What file number is the front cover? "))

outputFile = raw_input("What file to do you want to write this to? ")

writeFile(finalNumber, readingStartNum, fileType, outputFile)