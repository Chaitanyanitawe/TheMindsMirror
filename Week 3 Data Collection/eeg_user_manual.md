# HOW TO OPERATE AN EEG 

## THE DEVICE

Our EEG device consists of 4 electrodes that we have to place on the head and 2 others that are supposed to remain behind the ears in contact with the skin at all times. This is necessary to get accurate readings as when the electrodes touch the skin, you get negative values. The device lights up green when it’s turned on and lights up blue when it’s connected to another device. Yellow is displayed when the device is on standby. While taking readings, be sure to check whether your device is still connected to the EEG device (it must be lighted up blue during the entire collection process).

## THE PROCESS

We show the participant the game on PsychoPy, displaying the numbers 0-9 and a non-numerical image. To collect EEG data, we run ‘pc.py’. We must first install pylsl, websocket-client, timeflux, timeflux-ui, timeflux_dsp from pip (package installer for Python)  Using LabRecorder, we collect the EEG readings for the time they see the image. This will create a total of 11 XDF files for each image that we individually convert to excel files by running ‘importpyxdf.py.’ Additionally, running ‘lsl.SleepyEEG’ will help you visualize the brain waves we can interpret through the EEG data(here we are using timeflux).

### OR

Using the pygame setup install pylsl, pygame,websocket-client and (liblsl install using the method defined for your OS). Now run main.py and enter the participant’s name and it will create a csv file along with markers for each run which will contain the data of all 11 images.

## THE CODE

The main.py contains a pygame code that displays 11 images- 1 non numerical and other numericals that is in a randomized order.Before the display of each image there are 2 crosshairs that have to be clicked to know if the user is paying attention.The first one is displayed on a random spot on your screen, the second one in the middle. The code continuously collects data and adds markers at the start and stop of an image stimulus.