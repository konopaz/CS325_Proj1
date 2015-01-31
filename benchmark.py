#!/usr/bin/env python

from algorithms import *
import sys, os, getopt, random, time

def printHelp():
  print
  print os.path.basename(sys.argv[0]) + " [--help|-h]",
  print "[(--algorithm|-a)=(enumeration|betterenum|divide|linear)] 1000"
  print
  print "Enter the name of the script, optional argument to specify the algorithm, "
  print "and the number of random data points to be generated."
  print 
  print "--algorithm,-a\t\tspecify and algorithm"
  print "--help,-h\t\tprint this help message"
  print
  print "Sample usage..."
  print "\t" + os.path.basename(sys.argv[0]) + " -a=linear 1000"
  print

def main(argv):

  try:
    opts, args = getopt.getopt(argv, "ha:", ["help", "algorithm=", "min=", "max="])
  except getopt.GetoptError:
    printHelp()
    exit(2)

  if len(args) == 0:
    printHelp()
    exit(2)

  selectedAlgorithm = "linear"
  randIntMax = 100
  randIntMin = -100

  try:
    randIntCnt = int(args[0])
  except ValueError:
    print "Couldn't parse ", argv[0], " as an int."
    printHelp()
    exit(2)

  for opt in opts:
    if opt[0] == "--algorithm" or opt[0] == "-a":

      if opt[1] in ["linear", "enumeration", "betterenum", "divide"]:
        selectedAlgorithm = opt[1]

    elif opt[0] == "--min":
      randIntMin = int(opt[1])

    elif opt[0] == "--max":
      randIntMax = int(opt[1])

    elif opt[0] == "--help" or opt[0] == "-h":
      printHelp()
      exit(2)

  print "Run the", selectedAlgorithm, "algorithm with", randIntCnt, "random ints..."

  randInts = []
  for i in range(0, randIntCnt):
    randInts.append(random.randint(randIntMin, randIntMax))

  startTime = time.clock()

  #print randInts
  if selectedAlgorithm == "enumeration":
    sumData = enumerationAlgorithm(randInts)
  elif selectedAlgorithm == "betterenum":
    sumData = betterEnumerationAlgorithm(randInts)
  elif selectedAlgorithm == "divide":
    sumData = divideAndConquerAlgorithm(randInts)
  elif selectedAlgorithm == "linear":
    sumData = linearAlgorithm(randInts)
  else:
    print "Unsupported algorithm: ", selectedAlgorithm
    exit(1)

  endTime = time.clock()

  print sumData
  print "took ", (endTime - startTime), " seconds"

if __name__ == "__main__":
  main(sys.argv[1:])
