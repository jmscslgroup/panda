#!/usr/bin/env python
# coding: utf-8

# # Script to record data from RAV4 Using Panda/Giraffe

# ## Install Panda

# In[ ]:


get_ipython().system('cd ..; python setup.py install')


# ## Install other necessary packages

# In[ ]:


get_ipython().system('pip install cantools tqdm libusb1 pyserial bitstring')


# ## Import  Packages

# In[ ]:


import binascii
import bitstring
import time
import datetime
import serial
import csv
import numpy as np
import matplotlib.pyplot as plt



import pandas as pd # Note that this is not commai Panda, but Database Pandas
import cantools 
import matplotlib.animation as animation
from matplotlib import style
import uuid


# ## Connect to Panda

# In[ ]:


from panda import Panda #Import Comma AI Panda
__vehicleName__ = 'Rav4'
panda = Panda()


# ## Record data in infinite loop

# ### To Stope recrod, go to Kernel -> Interrupt

# In[ ]:



# Create a Unique File Name
unique_filename = str(uuid.uuid4())
currTime = str(time.time())
dt_object = datetime.datetime.fromtimestamp(time.time())
dt = dt_object.strftime('%Y-%m-%d-%H-%M-%S-%f')
fileName = dt + '_' + unique_filename  + '_CAN_Message_'+__vehicleName__+'.csv'
rf_PANDA = open(fileName, 'a')
print('Writing: '+fileName)
csvwriter_PANDA = csv.writer(rf_PANDA)
csvwriter_PANDA.writerow(['Time','Bus', 'MessageID', 'Message', 'MessageLength'])

while True:
    can_recv = panda.can_recv() # collects packages, 256 at a time
    #print(can_recv)
    currTime = time.time() # Records time of collection
    for address, _, dat, src  in can_recv:
    	# Be careful changing this, can be picky:
    	csvwriter_PANDA.writerow(([str(currTime), str(src), str((address)), str(binascii.hexlify(dat).decode('utf-8')), len(dat)]))
    	#print('Addres: '+str((address)), end='\r')


# ## Load the decode py script _DBC_READ_Tools_

# In[ ]:


import DBC_Read_Tools as DBC


# ## Now read the csv file we saved above and use DBC decoder to decode messages and plot

# In[ ]:


can_data = pd.read_csv('CAN_Data_Giraffe.csv')# read in the data
#can_data = pd.read_csv(fileName)
db_file = cantools.db.load_file('newToyotacode.dbc')# Specify your dbc file


# ### Decode and Plot

# In[ ]:



# %% Plot the speed of the vehicle:
DBC.plotDBC('SPEED',1,can_data,db_file)


# In[ ]:




DBC.plotDBC('GAS_PEDAL',0,can_data,db_file)


DBC.plotDBC('ACC_CONTROL',2,can_data,db_file)


DBC.plotDBC('KINEMATICS',-1,can_data,db_file)

DBC.plotDBC('KINEMATICS',0,can_data,db_file)

DBC.plotDBC('KINEMATICS',1,can_data,db_file)

DBC.plotDBC('UKNOWN186',0,can_data,db_file)


DBC.plotDBC('UKNOWN291',0,can_data,db_file)
DBC.plotDBC('UKNOWN291',1,can_data,db_file)
DBC.plotDBC('UKNOWN291',2,can_data,db_file)

DBC.plotDBC('UKNOWN296',0,can_data,db_file)
DBC.plotDBC('UKNOWN296',1,can_data,db_file)
DBC.plotDBC('UKNOWN296',2,can_data,db_file)


#DBC.plotDBC('ACCELEROMETER', 0, can_data, db_file)

# %% Plot the estimated longitudonal radar measurements for track 0 and its relative speed:
DBC.plotDBC('TRACK_A_0',1,can_data,db_file)


DBC.plotDBC('TRACK_A_0',4,can_data,db_file)
# Note: Change the track number (for instance to TRACK_A_0) to see what other
# tracks are reporting.

# %% Clean and plot the distance measurements a bit:

# Extract data as a numpy array:
Distance_Data = DBC.getNumpyData('TRACK_A_1',1,can_data,db_file)
Rel_Speed_Data = DBC.getNumpyData('TRACK_A_1',4,can_data,db_file)
# This filters out distance measurements over 300:
Distance_Data = DBC.cleanDistanceData(Distance_Data)

print('Data Cleaned')
# %% Plot Cleaned Distance:
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
ax.minorticks_on()
ax.tick_params(axis="x", labelsize=18)
ax.tick_params(axis="y", labelsize=18)
ax.grid(which='major', linestyle='-', linewidth='0.5', color='blue')
ax.grid(which='minor', linestyle='--', linewidth='0.25', color='gray')
ax.set_xlabel('Time', fontsize=18)
ax.set_ylabel('Message', fontsize=18)
ax.set_title('Longitudinal Distance Measurements - Cleaned',fontsize= 20)

plt.plot(Distance_Data[:,0],Distance_Data[:,1],'.')


# In[ ]:


DBC.plotDBC('STEERING_LKA',0,can_data,db_file)


# In[ ]:


DBC.plotDBC('STEERING_LKA',1,can_data,db_file)


# In[ ]:


DBC.plotDBC('STEERING_LKA',2,can_data,db_file)


# In[ ]:


DBC.plotDBC('STEERING_LKA',3,can_data,db_file)


# In[ ]:


DBC.plotDBC('STEERING_LKA',4,can_data,db_file)


# In[ ]:



# %% Plot the estimated longitudonal radar measurements for track 0 and its relative speed:
DBC.plotDBC('TRACK_A_0',1,can_data,db_file)
DBC.plotDBC('TRACK_A_1',1,can_data,db_file)
DBC.plotDBC('TRACK_A_2',1,can_data,db_file)

