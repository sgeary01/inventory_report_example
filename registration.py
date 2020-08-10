'''
Copyright 2020 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Sat Aug 08 2020
File : registration.py
'''

import sys
import os
import stat
import logging
import argparse

import CodeInsight_RESTAPIs.reports.get_reports
import CodeInsight_RESTAPIs.reports.create_report
import CodeInsight_RESTAPIs.reports.delete_report

#####################################################################################################
#  Report Details
reportName = "Template Example Report"  # What is the name to be shown within Code Insight?
enableProjectPickerValue = "false"   # true if a second project can be used within this report

# The path with the custom_report_scripts folder to called via the framework
if sys.platform.startswith('linux'):
    reportPath = "sca-codeinsight-reports-template/create_report.sh" 
elif sys.platform == "win32":
    reportPath = "sca-codeinsight-reports-template/create_report.bat"
else:
    sys.exit("No script file for operating system")

#-----------------------------------------------------------------------------------------------------
domainName = "UPDATEME"
port = "UPDATEME"
adminAuthToken = "UPDATEME"

# Quick sanity check
if adminAuthToken == "UPDATEME":
    print("Make sure domainName, port and the admin authorization token have been updated within registration.py")
    sys.exit()

###################################################################################
# Test the version of python to make sure it's at least the version the script
# was tested on, otherwise there could be unexpected results
if sys.version_info <= (3, 5):
    raise Exception("The current version of Python is less than 3.5 which is unsupported.\n Script created/tested against python version 3.8.1. ")
else:
    pass

###################################################################################
#  Set up logging handler to allow for different levels of logging to be capture
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S',

filename="_custom_report_registration.log", filemode='w',level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create command line argument options
parser = argparse.ArgumentParser()
parser.add_argument('-reg', "--register", action='store_true', help="Register custom reports")
parser.add_argument("-unreg", "--unregister", action='store_true', help="Unegister custom reports")

#----------------------------------------------------------------------#
def main():
    # See what if any arguments were provided
    args = parser.parse_args()

    if args.register and args.unregister:
        # You can use both options at the same time
        parser.print_help(sys.stderr)
    elif args.register:
        register_custom_reports()
        if sys.platform.startswith('linux'):
            # Make the shell script executable
            os.chmod(reportPath, os.stat(reportPath).st_mode | stat.S_IEXEC)
    elif args.unregister:
        unregister_custom_reports()
    else:
        parser.print_help(sys.stderr)

#-----------------------------------------------------------------------#
def register_custom_reports():
    logger.debug("Entering register_custom_reports")

    # Get the current reports so we can ensure the indexes of the new
    # reports have no conflicts
    try:
        currentReports = CodeInsight_RESTAPIs.reports.get_reports.get_currently_registered_reports(domainName, port, adminAuthToken)
    except:
        logger.error("Unable to retreive currently registered reports")
        print("Unable to retreive currently registered reports.  See log file for details")
        return -1

    # Determine the maximun ID of any current report
    maxReportOrder = max(currentReports, key=lambda x:x['id'])["order"]
    reportOrder = maxReportOrder + 1

    logger.info("Attempting to register %s with a report order of %s" %(reportName, reportOrder))
    print("Attempting to register %s with a report order of %s" %(reportName, reportOrder))

    try:
        reportID = CodeInsight_RESTAPIs.reports.create_report.register_report(reportName, reportPath, reportOrder, enableProjectPickerValue, domainName, port, adminAuthToken)
        print("%s has been registed with a report ID of %s" %(reportName, reportID))
        logger.info("%s has been registed with a report ID of %s" %(reportName, reportID))
    except:
        logger.error("Unable to register report %s" %reportName)
        print("Unable to register report %s.  See log file for details" %reportName)
        return -1


#-----------------------------------------------------------------------#
def unregister_custom_reports():
    logger.debug("Entering unregister_custom_reports")

    try:
        CodeInsight_RESTAPIs.reports.delete_report.unregister_report(domainName, port, adminAuthToken, reportName)
        print("%s has been unregisted." %reportName)
        logger.info("%s has been unregisted."%reportName)
    except:
        logger.error("Unable to unregister report %s" %reportName)
        print("Unable to unregister report %s.  See log file for details" %reportName)
        return -1
    


  
#----------------------------------------------------------------------#    
if __name__ == "__main__":
    main()    
