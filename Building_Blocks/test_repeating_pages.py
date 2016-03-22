import re, os

# To-do: set variables. If the page IN the list, THEN the variable now == that page.

# Determines the length of the 000s to ensure that the filename is 8 characters.
def determinePrefixLength(fileNum):
	global prefixZeroes
	if 0 < fileNum < 10:
		prefixZeroes = '0000000'
	elif 10 <= fileNum < 100:
		prefixZeroes = '000000'
	elif 100 <= fileNum < 1000:
		prefixZeroes = '00000'
	elif 1000 <= fileNum < 10000:
		prefixZeroes = '0000'
	else:
		prefixZeroes = 'error'

# Creates the file's name. Combines the leading 0s, integer as string, and filetype, and outputs global variable fileName
def generateFileName(prefix, suffix, fileType):
	global fileName
	fileName = prefix + str(suffix) + '.' + fileType.lower()

#  Uses the number of the reading start page to determine where the reading order starts/print.
def generateOrderLabel(readingStartNum, readingEndNum, fileNum, orderNum, romanStart, romanCap, romanInt):
	global orderLabel
	orderLabel = ''
	if romanCap != 0:
		if fileNum >= romanStart and romanInt <= romanCap:
			orderLabel = 'orderlabel: "' + toRoman(romanInt) + '"'
		elif romanCap < romanInt:
			orderLabel = ''
	if readingStartNum <= fileNum <= readingEndNum and fileNum not in unpaginatedPages:
		orderLabel = 'orderlabel: "' + str(orderNum) + '"'

# Adds conversion support to/from Roman numerals, taken from diveintopython.net examples
romanNumeralMap = (('m',  1000),
				('cm', 900),
				('d',  500),
				('cd', 400),
				('c',  100),
				('xc', 90),
				('l',  50),
				('xl', 40),
				('x',  10),
				('ix', 9),
				('v',  5),
				('iv', 4),
				('i',  1))

def toRoman(n):
	result = ''
	for numeral, integer in romanNumeralMap:
		while n >= integer:
			result += numeral
			n -= integer
	return result

def fromRoman(s):
	result = 0
	index = 0
	for numeral, integer in romanNumeralMap:
		while s[index:index+len(numeral)] == numeral:
			result += integer
			index += len(numeral)
	return result

# Processes inputs for various page numbers. Casts everything but covers, because there should only be one, into lists if they're not already lists. Could almost definitely be improved.
def inputToLists():
	global blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, multiworkBoundaries, prefacePages, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages, unpaginatedPages
	if type(blankPages).__name__ == 'int':
		blankPages = [blankPages]
	if type(chapterPages).__name__ == 'int':
		chapterPages = [chapterPages]
	if type(chapterStart).__name__ == 'int':
		chapterStart = [chapterStart]
	if type(copyrightPages).__name__ == 'int':
		copyrightPages = [copyrightPages]
	if type(firstChapterStart).__name__ == 'int':
		firstChapterStart = [firstChapterStart]
	if type(foldoutPages).__name__ == 'int':
		foldoutPages = [foldoutPages]
	if type(imagePages).__name__ == 'int':
		imagePages = [imagePages]
	if type(indexStart).__name__ == 'int':
		indexStart = [indexStart]
	if type(multiworkBoundaries).__name__ == 'int':
		multiworkBoundaries = [multiworkBoundaries]
	if type(prefacePages).__name__ == 'int':
		prefacePages = [prefacePages]
	if type(unpaginatedPages).__name__ == 'int':
		unpaginatedPages = [unpaginatedPages]
	if type(referenceStartPages).__name__ == 'int':
		referenceStartPages = [referenceStartPages]
	if type(tableOfContentsStarts).__name__ == 'int':
		tableOfContentsStarts = [tableOfContentsStarts]
	if type(titlePages).__name__ == 'int':
		titlePages = [titlePages]
	if type(halfTitlePages).__name__ == 'int':
		halfTitlePages = [halfTitlePages]

# Handles the reading labels. Uses list function which then gets split apart, so that multiple labels can apply to same page if relevant.
def generateLabel(fileNum):
	global label
	inputToLists()
	labelList = []
# Testing whether or not a page has a label
	if fileNum == frontCover:
		labelList.append('"FRONT_COVER"')
	if fileNum == backCover:
		labelList.append('"BACK_COVER"')
	if fileNum in blankPages:
		labelList.append('"BLANK"')
	if fileNum in chapterPages:
		labelList.append('"CHAPTER_PAGE"')
	if fileNum in chapterStart:
		labelList.append('"CHAPTER_START"')
	if fileNum in copyrightPages:
		labelList.append('"COPYRIGHT"')
	if fileNum in firstChapterStart:
		labelList.append('"FIRST_CONTENT_CHAPTER_START"')
	if fileNum in foldoutPages:
		labelList.append('"FOLDOUT"')
	if fileNum in imagePages:
		labelList.append('"IMAGE_ON_PAGE"')
	if fileNum in indexStart:
		labelList.append('"INDEX"')
	if fileNum in multiworkBoundaries:
		labelList.append('"MULTIWORK_BOUNDARY"')
	if fileNum in prefacePages:
		labelList.append('"PREFACE"')
	if fileNum in referenceStartPages:
		labelList.append('"REFERENCES"')
	if fileNum in tableOfContentsStarts:
		labelList.append('"TABLE_OF_CONTENTS"')
	if fileNum in titlePages:
		labelList.append('"TITLE"')
	if fileNum in halfTitlePages:
		labelList.append('"TITLE_PARTS"')
	if not labelList:
		label = ''
	else:
		label = 'label: ' + ', '.join(labelList)

# Combines all functions to write the file.
def writeFile(finalNumber, readingStartNum, readingEndNum, fileType, outputFile, romanCap, workingDir):
	originalDir = os.getcwd()
	os.chdir(workingDir)
	f = open(outputFile, 'w')
	f.write('pagedata:\n')
	fileNum = 1
	orderNum = 1
	if romanCap != '':
		romanInt = 1
	while fileNum <= finalNumber:
		determinePrefixLength(fileNum)
		generateFileName(prefixZeroes, fileNum, fileType)
		generateOrderLabel(readingStartNum, readingEndNum, fileNum, orderNum, romanStart, romanCap, romanInt)
		generateLabel(fileNum)
		comma = ''
		if orderLabel != '' and label !='':
			comma = ', '
		output = '    ' + fileName + ': { ' + orderLabel + comma + label + ' }\n'
		f.write(output)
		if fileNum >= romanStart and romanInt <= romanCap:
			romanInt += 1
		if readingStartNum <= fileNum <= readingEndNum and fileNum not in unpaginatedPages:
			orderNum += 1
		fileNum += 1
	f.close()
	print "File " + outputFile + " created in " + workingDir
	os.chdir(originalDir)

# Putting input into a function vs. having a huge list of inputs at the end.
def gatherInput():
	global fileType, workingDir, finalNumber, readingStartNum, readingEndNum, frontCover, outputFile, backCover, blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, multiworkBoundaries, prefacePages, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages, romanStart, romanCap, scanYearMonthDay, scanTime, DST, scannerModelInput, scannerMakeInput, bitoneResInput, contoneResInput, compressionDST, imageCompression, imageCompressionTime, imageCompressionTool, imageCompressionYearMonthDay, imageCompressionTime, imageCompressionAgent, imageCompressionToolList, scanningOrderInput, readingOrderInput, unpaginatedPages
	print 'INSTRUCTIONS:\n1. When listing multiple numbers, separate with a comma and space, e.g. "1, 34"\n\n2. Some entries such as first chapter should only have multiple entries if multiple works are bound together, such as two journal volumes.\n\n3. When a question doesn\'t apply and isn\'t Y/N, ENTER 0. Not entering anything will confuse the program.\n\n4. Do not use quotation marks.\n'
	workingDir = "/users/rtillman/documents/projects/hathitrust"
	outputFile = "meta_test_py.yml"
	fileType = "tif"
	finalNumber = "360"
	frontCover = "1"
	halfTitlePages = "0"
	titlePages = "13, 189"
	copyrightPages = "14, 190"
	tableOfContentsStarts = "356"
	romanStart = "0"
	romanCap = "0"
	prefacePages = "0"
	readingStartNum = "13, 189"
	firstChapterStart = "15, 191"
	chapterPages = "0"
	chapterStart = input("List file numbers of the start of each chapter **EXCEPT** the first, including appendices: ")
	readingEndNum = input("What is the file number on which the final NUMBERED page occurs? ")
	blankPages = input("List the file numbers of any blank pages: ")
	unpaginatedPages = input("List the file numbers of any pages outside the pagination sequence (not unpaginated but entirely skipped, such as photographic inserts): ")
	imagePages = input("List the file number of any page which is only an image: ")
	foldoutPages = input("List the file number of any page that is a scan of a foldout: ")
	indexStart = input("List the file number of any pages which are the FIRST page of an index: ")
	referenceStartPages = input("List the file number of the first page of any set of references or bibliography: ")
	multiworkBoundaries = input("List the file number of any multi-work boundaries: ")
	backCover = input("What is the file number of the back cover? ")

gatherInput()
writeFile(finalNumber, readingStartNum, readingEndNum, fileType, outputFile, romanCap, workingDir)
