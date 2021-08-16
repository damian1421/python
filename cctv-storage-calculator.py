#Description: Utility to caculate storage needed for CCTV storage.
#Author: l0gg3r
#Date: 2021-08-16
import os

clear = lambda: os.system('clear') #Define 'clear' command

try:
    nl = '\n' #Variable for new lines
    clear() #Clear screen
    nl
    print ("CCTV Storage Calculator") #Greetings

    #Complete with the requested info to start the calculation
    server = input('Server: ')
    cameras = int(input('Number of cameras: '))

    VBR = input('Is VBR? Yes-No: ') #If VBR == 'yes' then set adaptative bitrate
    if 'y' in VBR or 'Y' in VBR:
        cam_min_bitrate = int(input('Min Kbps (Kilobits x second) by camera: '))
        quality = int(input('Quality 1-10 (10 is the best): '))
    
    cam_max_bitrate = int(input('Max Kbps (Kilobits x second) by camera: '))
    retention_days = int(input('Retention days: '))
    
    #Max TB needed for retention period
    max_retention_TB = float(cameras #Number of cameras
                            * cam_max_bitrate / 8 #Max KBps used by camera
                            * 86400 # KB in a day (KB per day = KBps * 60 * 60 * 24 )
                            / 1073741824 # Convert KB to TB in a day (TB = KB / 1024 / 1024 /1024 )
                            * retention_days
                            )

    #Print results for VBR
    if 'y' in VBR or 'Y' in VBR:
        #Min TB needed for retention period
        min_retention_TB = float(cameras #Number of cameras
                                * cam_min_bitrate / 8 #Min KBps used by camera
                                * 86400 # KB in a day (KB per day = KBps * 60 * 60 * 24 )
                                / 1073741824 # Convert KB to TB in a day (TB = KB / 1024 / 1024 /1024 )
                                * retention_days
                                )
        # Calculate average of VBR
        VBR_average = ( (max_retention_TB - min_retention_TB) * (quality / float(10)) + min_retention_TB)

        print (f"Storage needed for {cameras} cameras: {nl}\
               Min: {min_retention_TB:.2f} TB {nl}\
               Max: {max_retention_TB:.2f} TB")
        print (f"Will try to reach average of: {VBR_average:.2f} TB")
    else: #Print results for CBR
        print (f"Storage needed for {cameras} cameras: {max_retention_TB:.2f} TB")

    #Reverse calculation
    reverse_calculation = input('Would you like to check how many days you can store? Yes-No: ')
    if "y" in reverse_calculation or "Y" in reverse_calculation:
        how_many_TB = int(input("How many TB is in your storage?: "))
        how_many_days = int(how_many_TB / ((cameras * (cam_max_bitrate / 8 ))* 86400 / 1073741824))
        print(f"{how_many_TB} TB hold recordings of {cameras} cameras for {how_many_days} days.")
except Exception as error:
    print(f"Something has failed. Review code for {error}.")
finally:
    print (f"{nl} Finished")
