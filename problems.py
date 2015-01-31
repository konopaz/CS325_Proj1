#!/usr/bin/env python

from algorithms import *
import sys, os

def summary(fullArray, sumData):
  
  return str(fullArray) + ", " +\
    str(fullArray[sumData.left:sumData.right+1]) + ", " +\
    str(sumData.sum)

def printHelp():
  print "Sample usage..."
  print "\t" + os.path.basename(sys.argv[0]) + " someDataFile.txt"

class DataString:
  def __init__(self, dataString):
    self.dataString = dataString

  def parseFullArray(self):
    tmp = self.dataString[1:self.dataString.index("]")].split(", ")
    return [int(numeric_string) for numeric_string in tmp]

  def parseMaxSumSubArray(self):
    tmp = self.dataString.split("], ")[1]
    tmp = tmp[1:]
    tmp = tmp.split(", ")
    return [int(numeric_string) for numeric_string in tmp]

  def parseMaxSum(self):
    tmp = self.dataString[self.dataString.rfind(", ") + 2:]
    return int(tmp)

def main():

  if len(sys.argv) == 1:
    printHelp()
    exit(1)

  with open(sys.argv[1]) as dataFile:
    for line in dataFile:

      line = line.strip()
      dataString = DataString(line)
      fullArray = dataString.parseFullArray()

      print "From data file:\t\t\t", dataString.dataString
      print "From enum algo:\t\t\t", summary(fullArray, enumerationAlgorithm(fullArray))
      print "From better enum algo:\t\t", summary(fullArray, betterEnumerationAlgorithm(fullArray))
      print "From div & conq algo:\t\t", summary(fullArray, divideAndConquerAlgorithm(fullArray))
      print "From linear algo:\t\t", summary(fullArray, linearAlgorithm(fullArray))

if __name__ == "__main__":
  main()
