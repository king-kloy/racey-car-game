import cx_Freeze
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['Tk_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')


executables = [cx_Freeze.Executable("kloy.py")]

cx_Freeze.setup(
    name = "kloy 1.0",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files":[
                                 "car.png",
                                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')
                                 ]}},
    executables = executables
    )
