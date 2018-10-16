import sys
from cx_Freeze import setup, Executable
import os 

setup(
		name="inoutprocess",
		version="1.0",
		description = "algorithm test",
		author = "dap",
		executables = [Executable("inout_algorithm.py", base="Win32GUI")])

os.environ['TCL_LIBRARY'] = r'C:\Users\Minhae Kim\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Minhae Kim\Anaconda3\tcl\tk8.6'


#>python setupfio.py build  # 폴더 형식
#>python setupfio.py install  # 설치
