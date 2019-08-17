def isPrime(a):
  if a == 1:
    return False

  for i in range(2,a):
    if a % i ==0:
      return False
  return True


def isComposite(a):
  if a== 1:
    return False
  
  for i in range(2,a):
    if a % i ==0:
      return True
  return False


def factor_sum(a):
  factor_sum=0
  for i in range(1,a):
    if a % i ==0:
      factor_sum += i
  return factor_sum

def isPerfect(a):
  if factor_sum(a) ==a:
    return True
  return False

def isAbandant(a):
  if factor_sum(a) > a:
    return True
  return False

def isPosInt(a):
 # print "a is positive?: ", a>0, " and a is  Integer?: ", a==int(a)
  return a>0 and a==int(a)
  

import math
def checkSolution(x,y,z):
  delta = y**2-4*x*z
  if delta <0:
    return "No solution"
  if delta>=0:
    solution_1 = (-y+math.sqrt(delta))/(2*x)
    solution_2=  (-y-math.sqrt(delta))/(2*x)
    return isPosInt(solution_1) and isPosInt(solution_2)

def isTriangular(a):
  if isPosInt(a):
    checkSolution(0.5,0.5,a)
    
def isHexagonal(a):
  if isPosInt(a):
    checkSolution(2,-1,a)

  
a= raw_input("Enter a nunber: ")
a=int(a)
print "Is it a prime number?  ", isPrime(a)
print "Is it a composit number?  ", isComposite(a)
print "Is it a perfect number?  ", isPerfect(a)
print "Is it a abandant number?  ", isAbandant(a)
print "Is it a tiangular number?  ", isTriangular(a)
print "Is it a hexagonal number?  ", isHexagonal(a)
