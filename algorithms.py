class SumData:

  def __init__(self, left, right, sum):
    self.left = left
    self.right = right
    self.sum = sum

  def __str__(self):
    return '[' + str(self.left) + ',' + str(self.right) + '] = ' + str(self.sum)

def sumSubArray(fullArray, aRange):

  sum = 0
  for i in fullArray[aRange[0]:(aRange[1] + 1)]:
    sum = sum + i

  return sum

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

def linearAlgorithm(fullArray):
  
  retSumData = SumData(0, 0, fullArray[0])
  maxSoFar = fullArray[0]
  maxEndingHere = fullArray[0]

  for i in range(1, len(fullArray)):

    maxEndingHere = maxEndingHere + fullArray[i]

    if fullArray[i] > maxEndingHere:
      maxEndingHere = fullArray[i]
      retSumData.left = i
      
    if maxEndingHere > maxSoFar:
      maxSoFar = maxEndingHere
      retSumData.right = i

  retSumData.sum = maxSoFar

  return retSumData
