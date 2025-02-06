#ApproxPi.py
#Name:Ryder Anderson
#Date:02/02/2025
#Assignment:ApproxPI
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  precision = int(input("enter percision(1 to 10): "))
  precision = int(precision)
  
  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxpi = 4/1
  sign = -1 
  denom = 3 

  while round(approxpi , precision) != round(realPi , precision):
    print(approxpi)
    approxpi = approxpi + (sign * 4 / denom)

    sign = sign * -1
    denom = denom + 2



  
  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
