@echo off
::Activate virtual environment
source scrub~/bin/activate
::Run script
cmd /k python Scrubber.py
if %errorlevel% neq 0 echo An error occurred while running the script.