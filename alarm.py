
#A python program to set up an alarm 

from datetime import datetime
import winsound

alarm_time= input("Enter the time to be set as alarm(HH:MM:SS)- ")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
print("Setting up alarm....")

while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_second=now.strftime("%S")
    
    if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_second==current_second):
                    winsound.Beep(440, 500)
                    print("Wake Up!!")
                    break
