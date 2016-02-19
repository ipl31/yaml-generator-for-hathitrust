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

def generateLabel(pageNum):
	global label
	labelList = []
	blankPagesList = map(int, blankPages.split(", "))
# Multiple labels can be comma-separated...
	if pageNum == frontCover:
		labelList.append('"FRONT_COVER"')
	if pageNum == backCover:
		labelList.append('"BACK_COVER"')
	if pageNum in blankPagesList:
		labelList.append('"BLANK"')
	if not labelList:
		label = ''
	else:
		label = 'label: ' + ', '.join(labelList)

def writeFile(finalNumber, readingStartNum, fileType, outputFile):
	f = open(outputFile, 'w')
	pageNum = 1
	orderNum = 1
	while pageNum <= finalNumber:
		determinePrefixLength(pageNum)
		generateFileName(prefixZeroes, pageNum, fileType)
		generateOrderLabel(readingStartNum, pageNum, orderNum)
		generateLabel(pageNum)
		comma = ''
		if orderLabel != '' and label !='':
			comma = ', '
		output = '    ' + fileName + ': { ' + orderLabel + comma + label + ' }\n'
		f.write(output)
		if pageNum >= readingStartNum:
			orderNum += 1
		pageNum += 1
	f.close()


def gatherInput():
	global fileType, finalNumber, readingStartNum, frontCover, outputFile, backCover, blankPages
	outputFile = raw_input("What file to do you want to write this to? ")
	fileType = raw_input("What is the (lowercase) filetype? ")
	finalNumber = int(raw_input("What is the number of the final image? "))
	print 'When listing multiple numbers, separate them with a ", ".\nSome entries, such as the first chapter, should only have multiple entries if multiple works are bound together and submitted together, generally volumes of the same title. Occasionally something like Index may be repeated within a single work, such as a hymnal.\nWhen a question has no answer, ENTER 0.'
	readingStartNum = int(raw_input("What is the file number on which page 1 occurs? "))
	frontCover = int(raw_input("What file number is the front cover? "))
	backCover = int(raw_input("What is the file number of the back cover? "))
	blankPages = raw_input("List the file numbers of any black pages: ")

gatherInput()
writeFile(finalNumber, readingStartNum, fileType, outputFile)