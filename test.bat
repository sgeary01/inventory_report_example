@echo off
rem ################################################################################
rem #  This test file allows the report script to be called as if it was being
rem #  called from the custom report framework to allow for script development
rem #  prior to registering the script with Code Insight

set projectId=
set reportId=
set authToken=

./create_report.bat  %projectId%  %reportId%  %authToken%


