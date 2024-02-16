PyIOTech
========

Python wrapper for IOTech/Measurement-Computing data-acquisition devices. Updated to use 64-bit dll.

Keywords: DaqBoard, DaqBook, DaqLab, DaqScan, Personal Daq, TempBook, WaveBook.
<br>


## Example Usage ##

Read a single ADC sample from a single input channel:
```python
from __future__ import print_function, division
from PyIOTech import daq, daqh

device_name = b'DaqBoard3K0'
channel = 0
gain = daqh.DgainX1
flags = daqh.DafAnalog | daqh.DafUnsigned | daqh.DafBipolar | daqh.DafDifferential
max_voltage = 10.0
bit_depth = 16

try:
    dev = daq.daqDevice(device_name)
    data = dev.AdcRd(channel, gain, flags)
    # Convert sample from unsigned integer value to bipolar voltage.
    data = data*max_voltage*2/(2**bit_depth) - max_voltage
    print(data)
finally:
    dev.Close()
```

For more complex, commented examples, see the [examples](examples/) directory.
<br>


## Documentation ##

There is no official documentation for PyIOTech, however the python function-signature follows closely the C/C++ or Visual Basic function-signature, as documented in the [IOTech Programmer's Manual](IOTechProgrammersManual.pdf).  For the specific python API, consult the [source code](PyIOTech/daq.py) or the [examples](examples/).


## Installation ##

This is a pure python distribution with no external dependencies (except the IOTech device driver "daqx64.dll"). Tested with python 3.11 64 bits.
You can find the external dll at the [Diligent Software FTP server.](https://files.digilent.com/#downloads/iotech_software/DaqBoard_3000_Series_PCI_USB/)

To install, run: `$ pip install git+https://github.com/FranciscoGauna/PyIOTech`


## Credits ##

Heavily based on [pydaqboard](https://code.google.com/archive/p/pydaqboard/).


## License ##

[GNU General Public License, version 2](LICENSE.txt).
