# -*- coding: utf-8 -*-
# Author: Cyrill Lippuner
# Date: October 2018
"""
Driver file <Insert name/code if device>
<Insert description of device>
"""
import time                                                     # Imported for delay reasons
#################################################################
# TODO:
# Insert functionality directly into this template file
# OR
# Use a official driver of existing library, import it and map functionality
# import drivers.<_DRIVER> as <TEMPLATE_DRIVER>
#################################################################
import threading                                                # Threading class for the threads

from MuxModule import Mux                                       # SoftWEAR MUX module.

# Create a MUX shadow instance as there is only one Mux
MuxShadow = Mux()

# Unique identifier of the sensor
#################################################################
# TODO:
# In case the device supports an identification possibility
# IDENTIFIER = <TEMPLATE_DRIVER>.<DRIVER_ID>
#################################################################

# Addresses
#################################################################
# TODO:
# In case the device needs to be addressed via I2C, etc.
# ADDRESS = <TEMPLATE_DRIVER>.<DRIVER_ADDRESS>
# For I2C, bus number 2 should be used
# BUSNUM = 2
#################################################################


# Constants
#################################################################
# TODO:
# Add constants to be used for settings for example.
# MY_CONST = ...
#################################################################


#################################################################
# TODO:
# Fill in the definition fields <...> of the driver
#################################################################
class TEMPLATE:
    """Driver for <Device name>."""

    # Name of the device
    _name = '<Device name>'

    # Info of the device
    _info = '<Device description>'

    # Direction of the driver (in/out)
    _dir = '<Direction of data flow (in|out)>'

    # Dimension of the driver (0-#)
    _dim = <Dimension of the data vector (+int)>

    # Dimension map of the driver (0-#)
    _dimMap = <List of labels for each dimension>

    # Dimension unit of the driver (0-#)
    _dimUnit = <List of units for each dimension>

    # Channel
    #############################################################
    # For I2C, use channel
    # _channel = None
    # Else user pin
    # _pin = None
    #############################################################

    # Muxed channel
    #############################################################
    # For I2C, use channel
    # _muxedChannel = None
    # Else user pin
    # _muxedPin = None
    #############################################################

    # The driver object
    _driver = None

    # Flag whether the driver is connected
    _connected = False

    # Settings of the driver
    _settings = {
        #########################################################
        # Data refresh frequency
        # 'frequencies': [
        #     '1 Hz',
        #     '2 Hz',
        #     '3 Hz',
        #     '4 Hz',
        #     '5 Hz',
        #     '6 Hz',
        #     '10 Hz',
        #     '20 Hz',
        #     '30 Hz',
        #     '40 Hz',
        #     '50 Hz',
        #     '60 Hz',
        #     '100 Hz'
        # ],
        # Operation mode for driver
        # 'modes': [
        #     '<Mode 1>',
        #     '<Mode 2>',
        #     '<Mode 3>'
        # ],
        # Flags for driver
        # 'flags': ['<Driver flag>']
        #########################################################
    }

    # Data type of values
    _dataType = '<Type of values (Range|On/Off)>'

    # Data range for values
    _dataRange = <List of lower and upper bounds for the values ([]|[min,max])>

    # Value to set
    _currentValue = 0

    # Value history
    _values = None

    # Mode
    _mode = None

    # Duty frequency
    _dutyFrequency = None

    # Flags
    _flags = None

    # Frequency for the thread
    _frequency = '<default frequency>'

    # Period for the thread
    _period = <default period "1/<default frquency>">

    # Thread active flag
    _threadActive = False

    # Thread for the inner loop
    _thread = None

    # Duration needed for an update cycle
    _cycleDuration = 0


    def __init__(self, channel, muxedChannel = None, ADRSet = False):
        """Device supports an address pin, one can represent this with a 'True' value of ADRSet."""
        self._channel = channel                                 # Set pin
        self._muxedChannel = muxedChannel                       # Set muxed pin

        self._values = []                                       # Set empty values array

        #########################################################
        # Depending on which types of settings are enabled uncomment lines
        # self._mode = self._settings['modes'][<default mode>]  # Set default mode
        # self._frequency = self._settings['frquency'][<default frequency>] # Set default frequency
        # self._dutyFrequency = self._settings['modes'][<default dutyFrequency>] # Set default dutyFrequency
        # self._flags = <List of default flags>                 # Set default flag list
        #########################################################

        self._driver = <TEMPLATE_DRIVER>.<DRIVER>(address=ADDRESS_1,busnum=BUSNUM) # Create the driver object
        try:
            #####################################################
            # TODO:
            # Try to connect to the driver
            # Fail with error if not possible
            #####################################################
        except:
            self._connected = False

    def cleanup(self):
        """Clean up driver when no longer needed."""
        self._connected = False                                 # Device disconnected
        self._threadActive = False                              # Unset thread active flag
        #####################################################
        # TODO:
        # Disconnect from the device
        #####################################################

    def getDeviceConnected(self):
        """Return True if the device is connected, false otherwise."""
        try:
            #####################################################
            # TODO:
            # Try to verify identity of connected device
            # Fail with error if not confirmation
            #####################################################
        except:
            self._connected = False                             # Device disconnected
        return self._connected

    def configureDevice(self):
        """Once the device is connected, it must be configured."""
        try:
            #####################################################
            # TODO:
            # Configure device for start up
            # Fail with error if not confirmation
            #####################################################
        except:                                                 # Device disconnected in the meantime
            raise Error('Error on device while configuring')
        self._threadActive = True                               # Set thread active flag
        self._thread = threading.Thread(target=self._loop, name=self._name) # Create thread
        self._thread.daemon = True                              # Set thread as daemonic
        self._thread.start()                                    # Start thread

    def _loop(self):
        """Inner loop of the driver."""
        while True:
            beginT = time.time()                                # Save start time of loop cycle

            #####################################################
            # TODO:
            # Implement data read/write function and store the value in self._currentValue
            # You can use the flag self._update to check if new data is available
            # Consider using try: .. except: ..
            #####################################################

            self._values.append([time.time(), self._currentValue]) # Save timestamp and value

            endT = time.time()                                  # Save start time of loop cycle
            deltaT = endT - beginT                              # Calculate time used for loop cycle
            self._cycleDuration = deltaT                        # Save time needed for a cycle
            if (deltaT < self._period):
                time.sleep(self._period - deltaT)               # Sleep until next loop period

            if not self._threadActive:                          # Stop the thread
                return

    def getValues(self, clear=True):
        """Get values for the i2c device."""
        if self._values == None:                                # Return empty array for no values
            return []
        values = self._values[:]                                # Get the values
        if clear:
            self._values = []                                   # Reset values
        return values                                           # Return the values


    def getDevice(self):
        """Return device name."""
        return self._name

    def getName(self):
        """Return device name."""
        if self._muxedChannel == None:
            return '{}@<Device connection type>[{}]'.format(self._name, self._channel)
        else:
            return '{}@<Device connection type>[{}:{}]'.format(self._name, self._channel, self._muxedChannel)

    def getDir(self):
        """Return device direction."""
        return self._dir

    def getDim(self):
        """Return device dimension."""
        return self._dim

    def getDimMap(self):
        """Return device dimension map."""
        return self._dimMap[:]

    def getChannel(self):
        """Return device channel."""
        return self._channel

    def getMuxedChannel(self):
        """Return device muxed channel."""
        return self._muxedChannel

    def getAbout(self):
        """Return device settings."""
        return {
            'info': self._info,
            'dimMap': self._dimMap[:],
            'dimUnit': self._dimUnit[:],
            'dataType': self._dataType,
            'dataRange': self._dataRange[:]
        }

    def getSettings(self):
        """Return device settings."""
        return self._settings

    def getCycleDuration(self):
        """Return device cycle duration."""
        return self._cycleDuration

    def getMode(self):
        """Return device mode."""
        # Can be ignored or deleted if mode is not supported by the driver
        return self._mode

    def setMode(self, mode):
        """Set device mode."""
        ############################################################
        # Can be ignored or deleted if mode is not supported by the driver
        ############################################################
        # if (mode in self._settings['modes']):
        #     # Do something based on the mode or throw an error
        # else:
        #     raise ValueError('mode {} is not allowed'.format(mode))
        ############################################################

    def getFlags(self):
        """Return device mode."""
        ############################################################
        # Can be ignored or deleted if flags is not supported by the driver
        ############################################################
        return self._flags[:]

    def getFlag(self, flag):
        """Return device mode."""
        ############################################################
        # Can be ignored or deleted if flags is not supported by the driver
        ############################################################
        return self._flags[flag]

    def setFlag(self, flag, value):
        """Set device flag."""
        ############################################################
        # Can be ignored or deleted if flags is not supported by the driver
        ############################################################
        if (flag in self._settings['flags']):
            if value:
                self._flags.append(flag)                            # Add the flag
            else:
                self._flags.remove(flag)                            # Remove the flag
        else:
            raise ValueError('flag {} is not allowed'.format(flag))

    def getFrequency(self):
        """Return device frequency."""
        ############################################################
        # Can be ignored or deleted if frequency is not supported by the driver
        ############################################################
        return self._frequency

    def setFrequency(self, frequency):
        """Set device frequency."""
        ############################################################
        # Can be ignored or deleted if frequency is not supported by the driver
        ############################################################
        if (frequency in self._settings['frequencies']):
            self._frequency = frequency
            self._period = 1./int(self._frequency[:-3])
        else:
            raise ValueError('frequency {} is not allowed'.format(frequency))

    def getDutyFrequency(self):
        """Return device duty frequency."""
        ############################################################
        # Can be ignored or deleted if dutyFrequency is not supported by the driver
        ############################################################
        return self._dutyFrequency

    def setDutyFrequency(self, dutyFrequency):
        """Set device duty frequency."""
        ############################################################
        # Can be ignored or deleted if dutyFrequency is not supported by the driver
        ############################################################
        raise ValueError('duty frequency {} is not allowed'.format(dutyFrequency))
