from PyIOTech.daq import GetDeviceList, daqDevice, DaqError
from PyIOTech.daqh import DiodtLocal8255, Diodp8255IR, DioepP2, Diodp8255A, Diodp8255B, Diodp8255C

print(GetDeviceList())
dev = daqDevice(b'DaqBoard3K0')
try:
    print(dev.Online())

    config = dev.IOGet8255Conf(0, 0, 0, 0)
    print(config)
    dev.IOWrite(DiodtLocal8255, Diodp8255IR, 0, DioepP2, config)
    val = 255
    dev.IOWrite(DiodtLocal8255, Diodp8255A, 0, DioepP2, val)
    dev.IOWrite(DiodtLocal8255, Diodp8255B, 0, DioepP2, val)
    dev.IOWrite(DiodtLocal8255, Diodp8255C, 0, DioepP2, val)
except DaqError as e:
    print(e.errcode)
    print(e.msg)
finally:
    dev.Close()