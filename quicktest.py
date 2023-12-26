from ctypes import CDLL
from ctypes.util import find_library

res = find_library("C:\\Windows\\SysWOW64\\DaqCOM2.dll")
lib = CDLL(res)
print(dir(lib))
