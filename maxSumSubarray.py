#!/usr/bin/env python

import sys, os

def enumerationAlgorithm(fullArray):

  fullArrayLength = len(fullArray)
  sumData = SumData(None, None, None)

  maxSum = None
  maxRange = None

  for i in range(fullArrayLength):

    for j in range(fullArrayLength):

      tmpRange = (i, j)
      tmpSum = sumSubArray(fullArray, tmpRange)

      if sumData.sum == None or sumData.sum < tmpSum:

        maxSum = tmpSum
        maxRange = tmpRange

        sumData.sum = tmpSum
        sumData.left = i
        sumData.right = j

  return sumData

def betterEnumerationAlgorithm(fullArray):

  fullArrayLength = len(fullArray)
  sumData = SumData(fullArray[0], None, None)

  for i in range(fullArrayLength):
    
    tmpSum = fullArray[i]

    if tmpSum > sumData.sum:
      sumData.sum = tmpSum
      sumData.left = i
      sumData.right = i

    for j in range(i + 1, fullArrayLength):

      tmpSum = tmpSum + fullArray[j]

      if(tmpSum > sumData.sum):
        sumData.sum = tmpSum
        sumData.left = i
        sumData.right = j

  return sumData

def divideAndConquerAlgorithm(fullArray, left=0, right=None):

  if right == None:
    right = len(fullArray) - 1

  if right == left:
    return SumData(left, left, fullArray[left])

  midpoint = (left + right) / 2

  retData = divideAndConquerAlgorithm(fullArray, left, midpoint)
  rightData = divideAndConquerAlgorithm(fullArray, midpoint + 1, right)
  if retData.sum < rightData.sum: retData = rightData
  
  sum = 0
  leftSum = None
  leftEdge = None

  for i in reversed(range(left, midpoint+1)):

    sum = sum + fullArray[i]

    if leftSum == None or sum > leftSum:
      leftSum = sum
      leftEdge = i

  sum = 0
  rightSum = None
  rightEdge = None
  
  for j in range(midpoint + 1, right + 1):

    sum = sum + fullArray[j]

    if rightSum == None or sum > rightSum:
      rightSum = sum
      rightEdge = j

  if leftSum + rightSum > retData.sum:
    retData = SumData(leftEdge, rightEdge, leftSum + rightSum)

  return retData

def sumSubArray(fullArray, aRange):

  sum = 0
  for i in fullArray[aRange[0]:(aRange[1] + 1)]:
    sum = sum + i

  return sum

def summary(fullArray, sumData):
  
  return str(fullArray) + ", " +\
    str(fullArray[sumData.left:sumData.right+1]) + ", " +\
    str(sumData.sum)

def printHelp():
  print "Sample usage..."
  print "\t" + os.path.basename(sys.argv[0]) + " someDataFile.txt"

class SumData:

  def __init__(self, left, right, sum):
    self.left = left
    self.right = right
    self.sum = sum

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

if __name__ == "__main__":
  main()
