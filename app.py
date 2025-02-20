import os
import shutil
import sys
import time
import pathlib
import subprocess

a = 1
b = 2

#MAP TO JETCAM ARCHIVE DIRECTORY
subprocess.call(r'net use o: /del', shell=True)
subprocess.call(r'net use o: \\SQLSVR2\Archive /user:SQLSVR2\admin m1lkman3', shell=True)

header = """  ___ ______  _____ _   _  ___  _____ _____ _  |___/___ _____ _____ _____ _____ 
 / _ \| ___ \/  __ \ | | |/ _ \|  ___|  _  | |   |  _  |  __ \_   _/  ___|_   _|
/ /_\ \ |_/ /| /  \/ |_| / /_\ \ |__ | | | | |   | | | | |  \/ | | \ `--.  | |  
|  _  |    / | |   |  _  |  _  |  __|| | | | |   | | | | | __  | |  `--. \ | |  
| | | | |\ \ | \__/\ | | | | | | |___\ \_/ / |___\ \_/ / |_\ \_| |_/\__/ / | |  
\_| |_|_| \_| \____|_| |_|_| |_|____/ \___/\_____/\___/ \____/\___/\____/  \_/ """

print(header)
print('')


while a != b:
    options = ['g','q','j','x']
    lookingFor = str(input('What are you looking for? GTINPUT (' + str(options[0]) + '), Quotation (' + str(options[1]) + ') , Jetcam (' + str(options[2]) + '),  Exit (' + options[3] + ') ').upper())

    archiveQuotePath = [r'D:\\Solidworks Archive\\', r'Location 2']
    archiveGTPath = [r'\\designsvr1\\terry\\Door History Old\\', r'Location 2']
    archiveJetPath = [r'\\SQLSVR2\\Archive\\JetCam old JCF and JNF files\\']

    liveQuotePath = r'\\designsvr1\\Solidworks\\Door Designer\\Specifications\\'
    liveGTPath = r'\\designsvr1\\terry\\door_history 1\\'
    liveJetPath = r'\\designsvr1\\\Doors\\\Customers2\\\Archeologist\\'



    if lookingFor == 'G':
        doorNumber = input('Enter the door number ')
        for locs in archiveGTPath:
            print('Checking ' + str(locs) + ' for door number ' + doorNumber)
            time.sleep(1)
            print('Digging..')
            time.sleep(1)
            print('Digging...')
            if os.path.isfile(str(locs) + doorNumber + '.xlsm'):
                shutil.move(str(locs) + doorNumber + '.xlsm', liveGTPath + doorNumber + '.xlsm')
                print('All done, files moved, have a lovely day :D')
                break
            else:
                print('No file found in the archive location. Big sad :(')
    elif lookingFor == 'Q':
        quoteNumber = input('Please enter the quote number! ')
        for locs in archiveQuotePath:
            print('Checking ' + str(locs) + ' for quote number ' + quoteNumber)
            time.sleep(1)
            print('Digging...')
            time.sleep(1)
            print('Digging...')

            if os.path.exists(locs + 'Project ' + quoteNumber + r'\\'):
                shutil.move(locs + 'Project ' + quoteNumber, liveQuotePath + 'Project ' + quoteNumber)
                print('All done! Files moved! Happy Quoting :)')
                break
            else:
                print('No files found in archive =o.!!!')
    elif lookingFor == 'J':
        doorNumber = input('Please enter the door number! ')
        for locs in archiveJetPath:
            print('Checking ' + str(locs) + ' for door number ' + doorNumber)
            time.sleep(1)
            print('Digging...')
            time.sleep(1)
            print('Digging...')

            count = 0
            for root,dirs,files in os.walk(locs):
                for file in files:
                    if file.startswith(doorNumber):
                        #print (root)
                        print("Moving File: " + str(file))
                        shutil.move(root + '\\' + file , liveJetPath + file)
                        count=+1

            if count == 0:
                print("No files found :(")
            else:
                print("All files have been moved to the jetcam Archeologist folder")


            #if os.path.isfile(str(locs) + doorNumber + '*' + '.JNF') or os.path.isfile(str(locs) + doorNumber + '*' + '.JGF'):
                #shutil.move(locs + 'Project ' + quoteNumber, liveQuotePath + 'Project ' + quoteNumber)
                #print('All done! Files moved! Happy Quoting :)')
                #break
            #else:
                #print('No files found in archive =o.!!!')
    elif lookingFor == 'X':
        print('Have a nice day :)')
        sys.exit()
    else:
        print('Enter a valid option: ' + str(options[0:10]))
