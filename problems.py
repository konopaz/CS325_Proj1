#!/usr/bin/env python

from algorithms import *
import sys, os, getopt

def summary(fullArray, sumData):
  
  if sumData == None:
    return str(fullArray) + ", empty, 0"

  return str(fullArray) + ", " +\
    str(fullArray[sumData.left:sumData.right+1]) + ", " +\
    str(sumData.sum)

def parseDataString(string):
  string = string.strip()
  string = string[1:len(string) - 1]
  data = string.split(", ")
  return [int(i) for i in data]

def printHelp():
  print
  print os.path.basename(sys.argv[0]) + " [--help|-h]",
  print "[(--algorithm|-a)=(enumeration|betterenum|divide|linear)] some-data-file.txt"
  print
  print "Enter the name of the script, optional arguments to specify the algorithm, "
  print "and the name of the file containing the problem data. The data file needs to "
  print "be in the format of [a, b, c, d] where the letters are integers with one line "
  print "print per array of data. The linear implementation is run by default."
  print 
  print "--file,-f\t\tspecify the output file, defaults to stdout"
  print "--algorithm,-a\t\tspecify and algorithm"
  print "--help,-h\t\tprint this help message"
  print
  print "Sample usage..."
  print "\t" + os.path.basename(sys.argv[0]) + " -a=linear some-data-file.txt"
  print

def main(argv):

  try:
    opts, args = getopt.getopt(argv, "hf:a:", ["help", "file=", "algorithm="])
  except getopt.GetoptError:
    printHelp()
    exit(2)

  if len(args) == 0:
    printHelp()
    exit(2)

  selectedAlgorithm = "linear"
  outFile = sys.stdout

  for opt in opts:
    if opt[0] == "--algorithm" or opt[0] == "-a":

      if opt[1] in ["linear", "enumeration", "betterenum", "divide"]:
        selectedAlgorithm = opt[1]

    elif opt[0] == "--file" or opt[0] == "-f":
      outFile = open(opt[1], 'w')

    elif opt[0] == "--help" or opt[0] == "-h":
      printHelp()
      exit(2)

  with open(args[0]) as dataFile:
    for line in dataFile:

      dataArray = parseDataString(line)

      if selectedAlgorithm == "enumeration":
        print >>outFile, summary(dataArray, enumerationAlgorithm(dataArray))
      elif selectedAlgorithm == "betterenum":
        print >>outFile, summary(dataArray, betterEnumerationAlgorithm(dataArray))
      elif selectedAlgorithm == "divide":
        print >>outFile, summary(dataArray, divideAndConquerAlgorithm(dataArray))
      elif selectedAlgorithm == "linear":
        print >>outFile, summary(dataArray, linearAlgorithm(dataArray))
      else:
        print "Unsupported algorithm: ", selectedAlgorithm
        exit(1)

if __name__ == "__main__":
  main(sys.argv[1:])
