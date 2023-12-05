@echo off
::Create a virtual environment
virtualenv scrub~
::Activate virtual environment
source scrub~/bin/activate
::Install libraries
pip install splinter
pip install bs4
::Delete the installer
del "%~f0"