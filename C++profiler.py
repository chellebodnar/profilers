#Inserts the right stuff to profile your C++ code

def profile(f):
	file = open(f, "r")
	outputFile = open("output.cpp", "w")
	fileLines = file.readlines()
	lineNumber = 2
	start = False
	for line in fileLines:
		lineNumber += 1
		if "return endOfMain;" in line:
				outputFile.write("for (map<int,int>::iterator it=myMap.begin(); it!=myMap.end(); ++it)\n")
				outputFile.write("""{cout << "line number " << it->first << " was run " << it->second << " times." << endl;}\n""")

		outputFile.write(line)

		if "using namespace std;" in line:
			outputFile.write("#include<map>\n")
			outputFile.write("map<int, int> myMap;")
		if "int main()" in line:
			start = True
		if start:
			if "{" in line:
				outputFile.write("if(myMap.find(" + str(lineNumber) + ") == myMap.end()){myMap[" + str(lineNumber) + "] = 1;}\n")
				outputFile.write("else{myMap[" + str(lineNumber) + "]++;}\n")
				lineNumber += 2
	file.close()
	outputFile.close()

profile("main.cpp")

