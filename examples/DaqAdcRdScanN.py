"""Read multiple ADC samples from multiple input channels."""
from __future__ import print_function, division
from PyIOTech import daq, daqh
from PyIOTech.daq import DaqError

# Device name as registered with the Windows driver.
device_name = b'DaqBoard3K0'
# Input channel numbers.
first_channel = 12
last_channel = 13
# Programmable amplifier with gain of 1.
gain = daqh.DgainX1
# Bipolar-voltage differential input, unsigned-integer readout.
flags = (
    daqh.DafAnalog | daqh.DafUnsigned  # Default flags.
    | daqh.DafBipolar | daqh.DafDifferential  # Nondefault flags.
    )
# max_voltage and bit_depth are device specific.
# Our device's bipolar voltage range is -10.0 V to +10.0 V.
max_voltage = 10.0
# Our device is a 16 bit ADC.
bit_depth = 16

dev = daq.daqDevice(device_name)
try:
    # Connect to the device.
    # Read one sample.
    data = dev.AdcRdScanN(first_channel, last_channel, 1000, 1000.0, gain, flags)
    # Convert sample from unsigned integer value to bipolar voltage.
    print(data)
except DaqError as e:
    print(e.msg)
    print(e.errcode)
finally:
    # Close the connection to the device even if an exception is raised.
    dev.Close()
