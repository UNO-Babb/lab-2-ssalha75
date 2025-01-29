#FutureTime.py
#Name: Sara Salha
#Date: 1/29/2025
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable

  now = datetime.datetime.now()
  currentHour = (now.hour - 6)
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours

  hours = input("Enter hours: ")
  hours = int(hours) #change from text to number
  futureHour = currentHour + hours
  futureHour = futureHour % 24

  #Ask user for minutes

  minutes = input("Enter minutes: ")
  minutes = int(minutes)
  futureMinute = currentMinute + minutes
  futureMinute = futureMinute % 60

  #Calculate the time after the user-supplied time has passed.

  strHour = str(futureHour)
  strMinute = str(futureMinute)

  #Do not use any if statements in calculating the time.
 
  if futureMinute < 10:
    strMinute = "0" + strMinute #add a leading zero to one digit minute

  #Output the future time in standard format "HH:MM"
 
  print(strHour + ":" + strMinute)

if __name__ == '__main__':
  main()
