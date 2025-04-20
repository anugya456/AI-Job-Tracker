@echo off
:loop
echo [INFO] Running Job Tracker at %TIME% on %DATE% >> job_tracker_log.txt
python "C:\Users\anugy\PERSONAL PROJECTS\Job Application Tracker AI\job_tracker.py"
echo [INFO] Job Tracker completed at %TIME% on %DATE% >> job_tracker_log.txt

:: Corrected timeout (8 hours)
timeout /t 28800 /nobreak >nul

goto loop
