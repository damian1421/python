#Description: Utility to caculate storage needed for CCTV storage.
#Author: l0gg3r
#Date: 2021-08-10
import os

clear = lambda: os.system('clear') #Define 'clear' command

try:
    nl = '\n' #Variable for new lines
    clear() #Clear screen
    nl
    print ("CCTV Storage Calculator") #Greetings

    #Complete with the requested info to start the calculation
    cameras = int(input('Number of cameras: '))
    VBR = input('Is VBR? Yes-No: ')
    if VBR == 'y' or VBR == 'Y':
        cam_min_bitrate = int(input('Min Kbps (Kilobits x second) x camera: '))
        quality = int(input('Quality 1-10(10 is the best): '))
    cam_max_bitrate = int(input('Max Kbps (Kilobits x second) x camera: '))
    retention_days = int(input('Retention days: '))
    retention_TB = int(cameras #Number of cameras
                       * cam_max_bitrate / 8 #Max bitrate used by each camera KBps
                       * 3600 #KBph in 1 hour
                       * 24 / 1024 #MBpd in 1 day
                       * retention_days / 1024 / float(1024) #Total retention days TB
                       )
    if VBR == 'n' or VBR == 'N': #Apply for CBR
        print (f"Storage needed for {cameras} cameras: {retention_TB} TB")
    else: #Apply for VBR
        min_retention_TB = int(cameras #Number of cameras
                       * cam_min_bitrate / 8 #Max bitrate used by each camera KBps
                       * 3600 #KBph in 1 hour
                       * 24 / 1024 #MBpd in 1 day
                       * retention_days / 1024 / 1024 #TB in total retention period
                       )
        VBR_adaptative = retention_TB - min_retention_TB # Search variation bitrate_min_to_max
        VBR_adaptative = VBR_adaptative * quality #This and next_row will set the percentage of the quality required over the prev_row
        VBR_adaptative = VBR_adaptative / float(10)
        print (f"Storage needed for {cameras} cameras: {nl}\
              Min: {min_retention_TB} TB {nl}\
              Max: {retention_TB} TB")
        print ("Will try to reach average of: ",min_retention_TB + VBR_adaptative, " TB")
except:
    print("Something has failed. Review code.")
