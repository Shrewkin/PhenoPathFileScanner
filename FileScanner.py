from msilib.schema import Directory
import os.path, time
import os
from posixpath import dirname
import sys, getopt

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def driver(inputDir, outputDir):
    outputLog = open(outputDir + "outputLog.txt", "w")
    
    fileTree = getListOfFiles(dirName=inputDir)
    for elm in fileTree:
        fileModifyDate = time.ctime(os.path.getmtime(elm))
        outputString = "Last Modified: %s" % fileModifyDate + " File Path: "+ elm
        
        if (outputString[23] + outputString[24] > '11'):
            if (outputString[19] + outputString[20] + outputString[21] == 'Mar'):
                if (outputString[37] + outputString[38] == '22'):
                    outputLog.write("Last Modified: " + fileModifyDate + " File Path: "+ elm + "\n")
        
    outputLog.close()

def main(argv):
    inputDir = ''
    outputDir = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["idir=", "odir="])
    except getopt.GetoptError:
        print('FileScanner.py -i <inputDir> -o <outputDir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("This is the help menu, to run the program type the following: \n" +
                  "FileScanner.py -i <Input Directory> -o <Output Directory>\n"+
                  "An example of an input and output directory is as follows: \n"+
                  "C:\\Users\\Striz\\Desktop\\PhenoPath\\FileScanner.py\n"+
                  "This file will scan through all files in a directory and might take a long time\n"+
                  "depending on the amount of files in a directory. Once the program is finished it\n"+
                  "will create a text document in the output directory with a report of what files\n"+
                  "were modified before a requested date.")
            sys.exit()
        elif opt in ("-i", "--idir"):
            inputDir = arg
        elif opt in ("-o", "--odir"):
            outputDir = arg
            
    driver(inputDir=inputDir, outputDir=outputDir)

if __name__ == "__main__":
    main(sys.argv[1:])