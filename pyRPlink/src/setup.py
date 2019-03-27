# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = { #"packages" : ["locale",],
#                     "excludes" : ["tkinter"], 
#                     "path"     : sys.path + ["module"],
                     }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

setup(
        name = "Scarico timbrature",
        version = "0.1",
        author = "Marco Natalini",
        description = "Legge le timbrature dai dispositivi. Converte gli Rfid in codice dipendente.",
        options = {"build_exe" :build_exe_options},
        executables = [Executable("pyRPlink.py", 
                                  base = base,
                                  icon= "Logo2015eu.ico", 
                                  targetName = "pyRPlink.exe")])
