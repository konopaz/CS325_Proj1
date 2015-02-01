#!/usr/bin/env python

from algorithms import *
import sys, os, getopt, random, time

def printHelp():
  print
  print os.path.basename(sys.argv[0]) + " [--help|-h]",
  print "[(--algorithm|-a)=(enumeration|betterenum|divide|linear)]"
  print
  print "Enter the name of the script, optional argument to specify the algorithm, "
  print "and the number of random data points to be generated."
  print 
  print "--algorithm,-a\tspecify and algorithm"
  print "--min\t\tminimum int for rand num gen, defaults to -100"
  print "--max\t\tmaximum int for rand num gen, defaults to 100"
  print "--steps\t\tdefaults to 1"
  print "--stepsize\t\tdefaults to 1000"
  print "--help,-h\tprint this help message"

  print
  print "Sample usage..."
  print "\t" + os.path.basename(sys.argv[0]) + " -a=linear"
  print

def main(argv):

  try:
    opts, args = getopt.getopt(argv, "ha:", ["help", "algorithm=", "min=", "max=", "steps=", "stepsize="])
  except getopt.GetoptError:
    printHelp()
    exit(2)

  selectedAlgorithm = "linear"
  randIntMax = 100
  randIntMin = -100
  steps = 1
  stepsize = 1000

  for opt in opts:
    if opt[0] == "--algorithm" or opt[0] == "-a":

      if opt[1] in ["linear", "enumeration", "betterenum", "divide"]:
        selectedAlgorithm = opt[1]

    elif opt[0] == "--min":
      randIntMin = int(opt[1])

    elif opt[0] == "--max":
      randIntMax = int(opt[1])

    elif opt[0] == "--steps":
      steps = int(opt[1])

    elif opt[0] == "--stepsize":
      stepsize = int(opt[1])

    elif opt[0] == "--help" or opt[0] == "-h":
      printHelp()
      exit(1)

  for step in range(1, steps + 1):

    randInts = []
    for i in range(0, step * stepsize):
      randInts.append(random.randint(randIntMin, randIntMax))

    startTime = time.clock()

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

    print str(step * stepsize) + "," + str(endTime - startTime)

if __name__ == "__main__":
  main(sys.argv[1:])
