#TempConvert.py
#Name:Ryder Anderson
#Date:02/05/2025
#Assignment:Lab 3 TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempf = input("enter a fahrenheit temperature")
  tempf = int(tempf)
  tempC = (tempf - 32) * 5/9
  tempC = round(tempC , 2)
  print(tempf, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
