#Inserts the right stuff to profile your Python code

def getSpace(line):
   stripped = line.lstrip()
   return line[:len(line) - len(stripped)]

def clearEmptyLines(f):
	file = open(f, "r")
	clean = open("cleanedFile.py", "w")
	fileLines = file.readlines()
	for line in fileLines:
		if len(line.lstrip()) > 0:
			clean.write(line)
	file.close()
	clean.close()

def profile(f):
	file = open(f, "r")
	outputFile = open("output.py", "w")
	fileLines = file.readlines()
	lineNumber = 1
	writeTime = False
	curLineLength = 0
	outputFile.write("myDict = {}\n")
	for line in fileLines:
		lineNumber += 1
		if writeTime == True:
			s = getSpace(line)
			outputFile.write(s + "if " + str(lineNumber) + " in myDict.keys():\n")
			outputFile.write(s + "\t" + "myDict[" + str(lineNumber) + "] += 1\n")
			outputFile.write(s + "else:\n")
			outputFile.write(s + "\t" + "myDict[" + str(lineNumber) + "] = 1\n")
			lineNumber += 4
		line = line.rstrip()
		if line[-1] == ":":
			writeTime = True
		else:
			writeTime = False

		outputFile.write(line + "\n")

			
	outputFile.write("for k in myDict.keys():\n")
	outputFile.write("""\tprint "line number " + str(k) + " was run " + str(myDict[k]) + " times." \n""")
	file.close()
	outputFile.close()


clearEmptyLines("test.py")
profile("cleanedFile.py")





